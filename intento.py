#!pip install nba_api
from requests import request
import json
from pprint import pprint
from nba_api.stats.static import players
from nba_api.stats.static import teams
#from nba_api.stats.endpoints import playercareerstats
#from nba_api.stats.endpoints import commonplayerinfos
#player_info.available_seasons.get_data_frame()
players = players.get_players()
teams = teams.get_teams()
#pprint(teams)
#pprint(players)
players.get_data_frames()