from pyspark import SparkConf
from pyspark import SparkContext
import tweepy

from processing_tools import get_media_url, get_type, print_as_tsv, get_users_from_list, \
    get_date, get_words


def get_all_tweets(screen_name, auth, init_date, final_date, filter_words):  # Collection of tweets
    # Twitter only allows access to a users most recent 3240 tweets with this method

    # authorize twitter, initialize tweepy
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=200, tweet_mode='extended', entities=True,
                                   extended_entities=True, include_rts=True)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest, tweet_mode='extended',
                                       entities=True, extended_entities=True)

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print("...%s tweets downloaded so far" % (len(alltweets)))

    # Spark configuration

    conf = SparkConf().setAppName("Try1").setMaster("local")
    sc = SparkContext(conf=conf)

    # Get tweets date, media, favorites, retweets and text
    tweets_first = sc.parallelize(alltweets).map(
        lambda s: (
            s.created_at, get_media_url(s), get_type(s), s.favorite_count, s.retweet_count, s.full_text, s.user.name))
    # Filter tweets and get only tweets between required dates

    filtered_tweets = tweets_first.filter(lambda s: s[0].date() >= init_date) \
        .filter(lambda s: s[0].date() <= final_date) \
        .map(
        lambda s: ((s[0].strftime("%Y-%m-%d %H:%M")), s[1], s[2], s[3], s[4], s[5].replace('\n', ' '), s[6]))

    filtered_tweets = filtered_tweets.filter(lambda tweet: any(word in tweet[5] for word in filter_words))\
        .persist()

    user_file = str(screen_name) + '.tsv'
    print_as_tsv(user_file, filtered_tweets)
    sc.stop()


def buscar_tweets(args, auth):
    user_list = get_users_from_list(args.usuarios)
    init_date = get_date(args.fecha_inicio)
    final_date = get_date(args.fecha_final)
    filter_words = get_words(args)

    for user in user_list:
        get_all_tweets(user, auth, init_date, final_date, filter_words)
