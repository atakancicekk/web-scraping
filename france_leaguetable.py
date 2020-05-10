import requests
from bs4 import BeautifulSoup



url = "https://www.scorespro.com/soccer/france/teams/paris-saint-germain-MzI5NQ==/"
html = requests.get(url).content


soup = BeautifulSoup(html, "html.parser")


mylist = soup.find("div", {"class": "standingsTaba"}).find_all("table", {"class": "blocks"})

print "#".ljust(3, " "), "", "Team".ljust(20, " "), "", "MP".rjust(2, " "), "", "W".ljust(2, " "), "", "D".ljust(3, " "), "", "L".ljust(3, " "), "", "Goals".ljust(10, " "), "", "+/-".ljust(5, " "), "", "Pts".ljust(3, " ")


for team in mylist:
    rank = team.find("td", {"class": "rank"}).text
    team_name = team.find("td", {"class": "team"}).find("a").text
    match_played = team.find("td", {"class": "mp"}).text
    win = team.find("td", {"class": "winx"}).text
    draw = team.find("td", {"class": "draw"}).text
    lost = team.find("td", {"class": "lost"}).text
    goals = team.find("td", {"class": "goalfa"}).text
    diff = team.find("td", {"class": "goaldiff"}).text
    pts = team.find("td", {"class": "point"}).text
    print rank.ljust(3, " "), "", team_name.ljust(20, " "), "", match_played.ljust(2, " "), "", win.ljust(2, " "), "", draw.ljust(3, " "), "", lost.ljust(3, " "), "", goals.ljust(10, " "), "", diff.ljust(5, " "), "", pts.ljust(3, " ")
