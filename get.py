import os
import csv
from bs4 import BeautifulSoup


def HTMLtoCSV(filein):
    csv = open("res.csv", "w")

    file_name = filein
    with open(file_name) as html_file:
        soup = BeautifulSoup(html_file)

    tweets = soup.findAll("div", {"class": "tweet"})

    print("Nombre de tweets :", len(tweets) - 1)
    for tweet in tweets:
        at = tweet.find("span", {"class": "username"})
        if at != None:
            name = at.get_text()

        date = tweet.find("a", {"class": "tweet-timestamp"})
        if date != None:
            time = date['title']

        text = tweet.find("p", {"class": "tweet-text"})
        if text != None:
            info = text.get_text().replace(",", "").replace("\n", "").replace('"', '')

        csv.write("{},{},{},\n".format(name, time, info))

    print("Nombre de tweets :", len(tweets) - 1)
