from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import GradientBoostingRegressor

import csv
import random
import math


# Custom MSE function
def MSE(pred, labels):
    summ = 0.0
    for ind, val in enumerate(pred):
        summ = summ + (pred[ind][0] - labels[ind][0]) ** 2
        summ = summ + (pred[ind][1] - labels[ind][1]) ** 2
    return math.sqrt(summ / len(pred))

# So we can random our data but keep it consistent :P
random.seed(10)


# Makes code look better
def load_data(filename, labeled=False):
    data = []
    labels = []
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            if not labeled:
                data.append(row[0])
            else:
                data.append(row[0])
                labels.append([float(row[1]), float(row[2])])
    if labeled:
        return data, labels
    else:
        return data

# Train model on given files and get prediction scores
def set_eval(f1, f2, f3):
    # Load data
    train_x, train_y = load_data(f1, True)
    test_x, test_y = load_data(f2, True)
    dev_x, dev_y = load_data(f3, True)

    # Bag of words approach
    count_vect = CountVectorizer()
    X_train_counts = count_vect.fit_transform(train_x + test_x + dev_x)
   
    # Train a model!
    klass = MultiOutputRegressor(GradientBoostingRegressor(random_state=0))
    klass.fit(X_train_counts.toarray()[0:784], train_y)

    # scores are MSE of actual
    score1 = MSE(klass.predict(X_train_counts.toarray()[0:784]), train_y)
    score2 = MSE(klass.predict(X_train_counts.toarray()[784:834]), test_y)
    score3 = MSE(klass.predict(X_train_counts.toarray()[834:]), dev_y)

    return score1, score2, score3

## Check accuracy of raw data

print(set_eval('../data/polisent_raw/train.csv', 
               '../data/polisent_raw/test.csv', 
               '../data/polisent_raw/dev.csv'))

## Check accuracy of reduced data

print(set_eval('../data/polisent_red/train.csv', 
               '../data/polisent_red/test.csv', 
               '../data/polisent_red/dev.csv'))

## Check accuracy of Varying Percentages of replacement


# 10%
print(set_eval('../data/polisent_syn/train_10.csv', 
               '../data/polisent_syn/test_10.csv', 
               '../data/polisent_syn/dev_10.csv'))

# 50%
print(set_eval('../data/polisent_syn/train_50.csv', 
               '../data/polisent_syn/test_50.csv', 
               '../data/polisent_syn/dev_50.csv'))

# 1000%
print(set_eval('../data/polisent_syn/train_100.csv', 
               '../data/polisent_syn/test_100.csv', 
               '../data/polisent_syn/dev_100.csv'))
