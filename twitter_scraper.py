from __future__ import absolute_import, print_function
import argparse
import sys

from tweepy import OAuthHandler
from scripts import buscar_tweets

# The consumer key and secret will be generated for you after

consumer_key = 'kKL59aSkx287Et5rWqyrfyNd2'
consumer_secret = 'BMwMcq5m6KpMxyNM6MZNHFx1LoX00bzJJApdofxVsn3MArQ2hq'

# After the step above, you will be redirected to your app's page.

# Create an access token under the the "Your access token" section
access_token = '860926487117090817-I0aqoabvgAeZqqPo6j57m9t1uvcdN2X'
access_token_secret = 'ozOq4lTG4LXiPxPlrgeBFX7Rt91u1BOTDyZ8P8n1C778u'


def main(args, auth):
    buscar_tweets(args, auth)


def parse_args(sys_args):
    parser = argparse.ArgumentParser()
    parser.add_argument("--usuarios", "-u", help="Lista separada por comas de usuarios que se quieran buscar")
    parser.add_argument("--fecha_inicio", "-i", help="Fecha de inicio con el formato: DD/MM/AAAA")
    parser.add_argument("--fecha_final", "-f", help="Fecha final con el mismo formato")
    parser.add_argument("--palabras", "-p", help="Lista de palabras separada por comas para filtrar tweets")
    return parser.parse_args(sys_args)


if __name__ == "__main__":
    command_arguments = parse_args(sys.argv[1:])
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    main(command_arguments, auth)
