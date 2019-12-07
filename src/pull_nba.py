import requests


stats_headers={ 'Host': 'stats.nba.com', 'User-Agent': 'Firefox/55.0', 'Accept': 'application/json text/plain, */*', 'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate', 'Referer': 'https://stats.nba.com/', 'x-nba-stats-origin': 'stats', 'x-nba-stats-token': 'true', 'DNT': '1', }
response = requests.get('https://stats.nba.com/stats/synergyplaytypes?LeagueID=00&PerMode=PerGame&PlayType=Isolation&PlayerOrTeam=P&SeasonType=Regular+Season&SeasonYear=2019-20&TypeGrouping=offensive', headers= stats_headers )
with open('leaguedash.json', 'wb') as f:
    f.write(response.content)



