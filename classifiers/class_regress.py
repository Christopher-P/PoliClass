from sklearn.linear_model import LogisticRegression
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.feature_extraction.text import CountVectorizer
import csv
import random
import math
import numpy as np

# So we can random our data but keep it consistent :D
random.seed(10)

def MSE(pred, labels):
    summ = 0.0
    for ind, val in enumerate(pred):
        summ = summ + (pred[ind][0] - labels[ind][0]) ** 2
        summ = summ + (pred[ind][1] - labels[ind][1]) ** 2
    return math.sqrt(summ / len(pred))

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

# Expects training file name
# Returns classification values of quotes
def classify(f1):

    train_x, train_y = load_data(f1, True)
    communist = load_data('../data/quotes/manifesto.txt')
    federalist = load_data('../data/quotes/federalist.txt')
    socalist = load_data('../data/quotes/mein_kampf.txt')

    count_vect = CountVectorizer()
    X_train_counts = count_vect.fit_transform(train_x + communist + federalist + socalist)

    klass = MultiOutputRegressor(GradientBoostingRegressor(random_state=0))
    klass.fit(X_train_counts.toarray()[0:len(train_x)], train_y)

    t = len(train_x)
    c = len(communist)
    f = len(federalist)
    s = len(socalist)

    score1 = np.average(klass.predict(X_train_counts.toarray()[t:t+c]     ), axis=0).tolist()
    score2 = np.average(klass.predict(X_train_counts.toarray()[t+c:t+c+f] ), axis=0).tolist() 
    score3 = np.average(klass.predict(X_train_counts.toarray()[t+c+f:]    ), axis=0).tolist()  
   
    return score1, score2, score3



## Train on full raw set
print(classify('../data/polisent_raw/full.csv'))

## Train on full reduced set
print(classify('../data/polisent_red/full.csv'))

## Train on varying percentages
# 10 %
print(classify('../data/polisent_syn/full_10.csv'))

# 50 %
print(classify('../data/polisent_syn/full_50.csv'))

# 100 %
print(classify('../data/polisent_syn/full_100.csv'))

