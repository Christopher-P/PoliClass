from sklearn.linear_model import LogisticRegression
import csv
import random
import math

def MSE(pred, labels):
    summ = 0.0
    for ind, val in enumerate(pred):
        summ = summ + (pred[ind][0] - labels[ind][0]) ** 2
        summ = summ + (pred[ind][1] - labels[ind][1]) ** 2
    return math.sqrt(summ / len(pred))

# So we can random our data but keep it consistent for breaks ;)
random.seed(10)

# Load data
train_x = []
train_y = []
with open('train.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        train_x.append(row[0])
        train_y.append([float(row[1]), float(row[2])])

test_x = []
test_y = []
with open('test.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        test_x.append(row[0])
        test_y.append([float(row[1]), float(row[2])])

dev_x = []
dev_y = []
with open('dev.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        dev_x.append(row[0])
        dev_y.append([float(row[1]), float(row[2])])


# Train a model!

from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(train_x + test_x + dev_x)


from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import GradientBoostingRegressor
klass = MultiOutputRegressor(GradientBoostingRegressor(random_state=0))
klass.fit(X_train_counts.toarray()[0:343], train_y)

print(MSE(klass.predict(X_train_counts.toarray()[0:343]), train_y))
print(MSE(klass.predict(X_train_counts.toarray()[343:393]), test_y))
print(MSE(klass.predict(X_train_counts.toarray()[393:]), dev_y))
