from tkinter import *
from PIL import Image, ImageTk
import yaml
from twitter import Api
import json

#Import API info
credentials = yaml.safe_load(open("credentials.yml"))
key = credentials['API_key']
seckey = credentials['API_secret_key']
token = credentials['Access_token']
sectoken = credentials['Access_token_secret']

print(credentials)

CONSUMER_KEY = key
CONSUMER_SECRET = seckey
ACCESS_TOKEN = token
ACCESS_TOKEN_SECRET = sectoken

api = Api(CONSUMER_KEY,
          CONSUMER_SECRET,
          ACCESS_TOKEN,
          ACCESS_TOKEN_SECRET)

USERS = ['@']

LANGUAGES = ['en']

with open('output.txt', 'a') as f:
    # api.GetStreamFilter will return a generator that yields one status
    # message (i.e., Tweet) at a time as a JSON dictionary.
    for line in api.GetStreamFilter(track=USERS, languages=LANGUAGES):
        if line['favourites_count'] > 100:
            print("--")
            print(line['favourites_count'])
            print(dir(line))
            #print(line.keys())
            print(line['text'])

            f.write(json.dumps(line))
            f.write('\n')
            f.write('\n')
        

'''
root = Tk()

def key(event):
    print("woo")
    print("pressed", repr(event.char))
    

def callback(event):
    print("clicked at", event.x, event.y)


image = Image.open("chart.png")
photo_image = ImageTk.PhotoImage(image)
label = Label(root, image = photo_image)
label.focus_set()
label.bind("<Key>", key)
label.bind("<Button-1>", callback)
label.pack()

root.mainloop()
'''

