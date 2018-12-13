import csv
import random

# So we can random our data but keep it consistent for breaks ;)
random.seed(10)


# Used for taking breaks between classifying sessions

tweets = []
labels_x = []
labels_y = []
with open('classified.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        tweets.append(row[0])
        labels_x.append(int(row[1]))
        labels_y.append(int(row[2]))

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

print(norm_x)
print(norm_y)


with open('norm.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    for ind, val in enumerate(tweets):
        spamwriter.writerow([val, norm_x[ind], norm_y[ind]])

