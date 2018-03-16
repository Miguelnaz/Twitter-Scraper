import datetime


def get_words(args):
    return args.palabras.lower().split(',')


def get_media_url(status):  # To trate exceptions in nule media tweets
    try:
        if 'media' in status.extended_entities:
            for med in status.extended_entities['media']:
                return med['url']
    except:
        return ""


def get_type(status):  # To trate exceptions in nule media tweets
    try:
        if 'media' in status.extended_entities:
            for med in status.extended_entities['media']:
                return med['type']
    except:
        return ""


def print_as_tsv(filename, rdd):
    lis = rdd.collect()
    with open(filename, 'a') as file:
        for e in lis:
            for row in range(len(e)):
                file.write(str(e[row]) + "\t")
            file.writelines("\n")
    file.close()


def get_users_from_list(users):
    user_list = []
    for user in users.split(','):
        user_list.append(user)
    return user_list


def get_date(date):
    date_sep = date.split('/')
    return datetime.date(int(date_sep[2]), int(date_sep[1]), int(date_sep[1]))
