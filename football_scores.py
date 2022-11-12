import requests
import json
url = "https://api.sofascore.com/api/v1/sport/football/events/live"

payload = ""
headers = {
    "authority": "api.sofascore.com",
    "cache-control": "max-age=0",
    "sec-ch-ua": "^\^"
}
#getting the API
response = requests.request("GET", url, data=payload, headers=headers)
#writing down the json data

jsondata = json.loads(response.text)

#looking over all the games
for game in jsondata['events']:
    league=game['tournament']['name']
    category=game['tournament']['category']['name']
    #as I am intersted in EPL I want to display just these games
    if league == 'Premier League' and category=='England':

        hometeam = game['homeTeam']['name']
        awayteam = game['awayTeam']['name']

        homescore = game['homeScore']['current']
        awayscore = game['awayScore']['current']
        print(league, " | ", hometeam, homescore, " - ", awayteam, awayscore)
