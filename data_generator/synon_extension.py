import csv
import random
import numpy as np

import nltk 
from nltk.corpus import wordnet

np.random.seed(10)

def get_syn(word):
    synonyms = [] 
    for syn in wordnet.synsets(word): 
        for l in syn.lemmas(): 
            synonyms.append(l.name()) 
    if len(synonyms) == 0:
        return word
    return np.random.choice(synonyms)

tweets = []
labels_x = []
labels_y = []
with open('../data_collector/classified.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        tweets.append(row[0])
        labels_x.append(int(row[1]))
        labels_y.append(int(row[2]))

# NEW in syn_data
# Randomly replace words in tweets
tweets_100 = []
tweets_50  = []
tweets_10  = []

# 100% replacement
for ind,val in enumerate(tweets):
    words = val.split(' ')
    for ind2, word in enumerate(words):
        if np.random.rand() < 1.0:
            words[ind2] = get_syn(word)
        else:
            continue
    tweets_100.append(' '.join(words))

# 50% replacement
for ind,val in enumerate(tweets):
    words = val.split(' ')
    for ind2, word in enumerate(words):
        if np.random.rand() < 0.5:
            words[ind2] = get_syn(word)
        else:
            continue
    tweets_50.append(' '.join(words))

# 10% replacement
for ind,val in enumerate(tweets):
    words = val.split(' ')
    for ind2, word in enumerate(words):
        if np.random.rand() < 0.1:
            words[ind2] = get_syn(word)
        else:
            continue
    tweets_10.append(' '.join(words))

# Get average without zeros
tmp_X = [x for x in labels_x if x != 0]
avg_X = sum(tmp_X)/len(tmp_X)
tmp_Y = [x for x in labels_y if x != 0]
avg_Y = sum(tmp_Y)/len(tmp_Y)

# Set zeros to average
for ind, val in enumerate(labels_x):
    if val == 0:
        labels_x[ind] = avg_X
        labels_y[ind] = avg_Y

# Normalize values
#lower, upper = -1, 1
min_x = min(labels_x)
max_x = max(labels_x)
min_y = min(labels_y)
max_y = max(labels_y)

norm_x = [(x - min_x) / (max_x - min_x) for x in labels_x]
norm_y = [(x - min_y) / (max_y - min_y) for x in labels_y]

#------#
with open('../data/polisent_syn/test_100.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    for ind, val in enumerate(tweets_100[0:50]):
        spamwriter.writerow([val, norm_x[ind], norm_y[ind]])

with open('../data/polisent_syn/dev_100.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    for ind, val in enumerate(tweets_100[50:100]):
        spamwriter.writerow([val, norm_x[ind], norm_y[ind]])

with open('../data/polisent_syn/train_100.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    for ind, val in enumerate(tweets_100[100:]):
        spamwriter.writerow([val, norm_x[ind], norm_y[ind]])

with open('../data/polisent_syn/full_100.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    for ind, val in enumerate(tweets_100):
        spamwriter.writerow([val, norm_x[ind], norm_y[ind]])
# ------#
with open('../data/polisent_syn/test_50.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    for ind, val in enumerate(tweets_50[0:50]):
        spamwriter.writerow([val, norm_x[ind], norm_y[ind]])

with open('../data/polisent_syn/dev_50.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    for ind, val in enumerate(tweets_50[50:100]):
        spamwriter.writerow([val, norm_x[ind], norm_y[ind]])

with open('../data/polisent_syn/train_50.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    for ind, val in enumerate(tweets_50[100:]):
        spamwriter.writerow([val, norm_x[ind], norm_y[ind]])

with open('../data/polisent_syn/full_50.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    for ind, val in enumerate(tweets_50):
        spamwriter.writerow([val, norm_x[ind], norm_y[ind]])
# ------#
with open('../data/polisent_syn/test_10.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    for ind, val in enumerate(tweets_10[0:50]):
        spamwriter.writerow([val, norm_x[ind], norm_y[ind]])

with open('../data/polisent_syn/dev_10.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    for ind, val in enumerate(tweets_10[50:100]):
        spamwriter.writerow([val, norm_x[ind], norm_y[ind]])

with open('../data/polisent_syn/train_10.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    for ind, val in enumerate(tweets_10[100:]):
        spamwriter.writerow([val, norm_x[ind], norm_y[ind]])

with open('../data/polisent_syn/full_10.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    for ind, val in enumerate(tweets_10):
        spamwriter.writerow([val, norm_x[ind], norm_y[ind]])

