from sklearn.linear_model import LogisticRegression
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.feature_extraction.text import CountVectorizer
import csv
import random
import math

def MSE(pred, labels):
    summ = 0.0
    for ind, val in enumerate(pred):
        summ = summ + (pred[ind][0] - labels[ind][0]) ** 2
    return math.sqrt(summ / len(pred))

# So we can random our data but keep it consistent for breaks ;)
random.seed(10)

# Load data
train_x = []
train_y = []
with open('../data/yelp/yelp_labelled.txt', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    for row in spamreader:
        train_x.append(row[0])
        train_y.append([float(row[1])])

test_x = train_x[0:50]
test_y = train_y[0:50]

dev_x = train_x[50:100]
dev_y = train_y[50:100]

# Train a model!

# Bag of words approach
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(train_x)

# Initiate a Classifier and fit it!
klass = MultiOutputRegressor(GradientBoostingRegressor(random_state=0))
klass.fit(X_train_counts.toarray()[100:], train_y[100:])

# Train score
print(MSE(klass.predict(X_train_counts.toarray()[100:]), train_y[100:]))
# Test score
print(MSE(klass.predict(X_train_counts.toarray()[0:50]), test_y))
# Dev score
print(MSE(klass.predict(X_train_counts.toarray()[50:100]), dev_y))
