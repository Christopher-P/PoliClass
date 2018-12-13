from tkinter import *
from PIL import Image, ImageTk
import csv
import random
import os

# So we can random our data but keep it consistent for breaks ;)
random.seed(10)


# Used for taking breaks between classifying sessions
current = 575
tweets = []
with open('raw.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        tweets.append(' '.join(row))

random.shuffle(tweets)


def log_class(x,y):
    global current
    with open('classified.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow([tweets[current], x, y])


def key(event):
    global current
    if event.char == ' ':
        log_class(0,0)
        current = current + 1
        os.system('clear')  # on linux / os x
        print(current)
        print(tweets[current])
    elif event.char == '\x1b':
        current = current + 1
        os.system('clear')  # on linux / os x
        print(current)
        print(tweets[current])
    else:
        print("UNKNOWN")

    
    

def callback(event):
    global current
    log_class(event.x, event.y)
    current = current + 1
    #print("clicked at", event.x, event.y)
    os.system('clear')  # on linux / os x
    print(current)
    print(tweets[current])

root = Tk()
image = Image.open("chart.png")
photo_image = ImageTk.PhotoImage(image)
label = Label(root, image = photo_image)
label.focus_set()
label.bind("<Key>", key)
label.bind("<Button-1>", callback)
label.pack()

print(tweets[current])

root.mainloop()
