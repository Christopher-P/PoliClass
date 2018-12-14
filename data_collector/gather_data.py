import yaml
from twitter import Api
import tweepy
import re, string
from random import shuffle
import csv
import json

def determine(x):
    # X is string
    if len(x) == 0:
        return True
    elif '@' in x:
        return True
    elif '#' in x[0]:
        return True
    elif "\n" in x:
        return True
    elif x[0:2] == "rt":
        return True
    elif x[0:4] == "http":
        return True
    elif not all(ord(c) < 128 for c in x):
        return True
    return False

# Text handler
def proc_text(text):
    text = text.lower()
    text = text.replace('&amp', '')
    text = text.replace('.', '')
    text = text.replace('-', '')
    text = text.replace(';', '')
    text = text.replace(':', '')
    text = text.replace('[', '')
    text = text.replace(']', '')
    text = text.replace('(', '')
    text = text.replace(')', '')
    text = text.replace(',', '')
    text = text.replace('?', '')
    text = text.replace('!', '')
    text = text.replace("'", '')
    text = text.replace('\"', '')
    text = text.replace('"', '')
    text = text.split(' ')
    text = [x for x in text if not determine(x)]
    l = len(text)
    text = ' '.join(text)
    #text = str(text.decode('utf8'))
    # print(text)
    return text, l

#Import API info
credentials = yaml.safe_load(open("credentials.yml"))
key = credentials['API_key']
seckey = credentials['API_secret_key']
token = credentials['Access_token']
sectoken = credentials['Access_token_secret']

# Consumer keys and access tokens, used for OAuth
consumer_key = key
consumer_secret = seckey
access_token = token
access_token_secret = sectoken

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# user list
#names = ['@VanJones68', '@realDonaldTrump', '@DemSocialists',
#         '@RichardBSpencer', '@Nigel_Farage', '@tltconsulting',
#         '@Pontifex', '@OttoWilde' , '@AnarchistNews',
#         '@LPNational', '@FreedomWorks', '@TheDemocrats',
#          '@jeremycorbyn', '@UKIP', @UKLabour]
names = ['@UKLabour']


for user in names:
    data = []
    count = 0
    print("Gathering: ", user)
    for status in tweepy.Cursor(api.user_timeline, screen_name=user, tweet_mode="extended").items():
        text, l = proc_text(status.full_text)
        if l < 5:
            continue
        data.append(text)
        count = count + 1
        if count >= 500:
            break

    # shuffle(data)
    with open('raw.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        for i in data:
            print([i])
            spamwriter.writerow([i])











