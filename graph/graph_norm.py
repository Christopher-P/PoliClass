import numpy as np
import matplotlib.pyplot as plt 
import csv
import matplotlib.image as mpimg
## Load data
tweets = []
labels_x = []
labels_y = []
with open('../data_collector/classified.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        if float(row[1]) == 0.0:
            continue
        tweets.append(row[0])
        labels_x.append(float(row[1]))
        labels_y.append(float(row[2]))

img=mpimg.imread('../data_collector/chart.png')
plt.imshow(img)
plt.scatter(labels_x, labels_y)
plt.show()

print("x mean:", sum(labels_x)/len(labels_x))
print("y mean:", sum(labels_y)/len(labels_y))
