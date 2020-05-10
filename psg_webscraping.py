import requests
from bs4 import BeautifulSoup



url = "https://www.scorespro.com/soccer/france/teams/paris-saint-germain-MzI5NQ==/"
html = requests.get(url).content


soup = BeautifulSoup(html, "html.parser")


mylist = soup.find("div", {"class": "compgrp"}).find_all("table", {"class": "blocks"})

print " "

print soup.find("h3", {"class": "blockBarLt"}).text

for i in mylist:
    date = i.find("td", {"class": "kick_t"}).text
    tournament = i.find("td", {"class": "tour"}).text
    acron = i.find("td", {"class": "acron"}).text
    score = i.find("td", {"class": "score"}).find("a").text

    try:
        home_team = i.find("td", {"class": "home_o uc"}).text
    except AttributeError:
        home_team = i.find("td", {"class": "home_o uc winteam"}).text


    try:
        away_team = i.find("td", {"class": "away_o uc winteam"}).text
    except AttributeError:
        away_team = i.find("td", {"class": "away_o uc"}).text


    print date, " ", tournament.ljust(5, " "), " ", acron.ljust(5, " "), " ", home_team.ljust(28, " "), " ", score.ljust(8, " "), " ", away_team