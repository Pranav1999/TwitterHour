import threading
import time
from tkinter import *
import tweepy

tweet = ""


def clicked(window, txt):
    global tweet
    # tweet = txt.get()
    tweet = ""
    if txt.get() != "":
        tweet = txt.get()
    window.destroy()


def takeTweetInput():
    window = Tk()
    window.title("What did you learn?")
    window.geometry('1000x200')
    lbl = Label(window, text="Hello")
    lbl.grid(column=0, row=0)
    txt = Entry(window, width=140)
    txt.grid(column=0, row=10)
    btn = Button(window, text="Tweet", command=lambda: clicked(window, txt))
    btn.grid(column=0, row=20)
    window.mainloop()


def get_api(cfg):
    auth = tweepy.OAuthHandler("consumer_token",
                               "consumer_secret")
    auth.set_access_token("access_token",
                          "access_token_secret")
    return tweepy.API(auth)


def tweetSomething():
    cfg = {
        "consumer_key": "value",
        "consumer_secret": "value",
        "access_token": "value",
        "access_token_secret": "value"
    }
    api = get_api(cfg)
    takeTweetInput()
    if tweet != "":
        status = api.update_status(status=tweet)
        print(status)


def main():
    while True:
        threadObj = threading.Thread(target=tweetSomething)
        threadObj.start()
        time.sleep(3600)


if __name__ == "__main__":
    main()
