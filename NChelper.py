from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import playergamelog

from PyQt5 import QtCore, QtWidgets, QtGui

import requests
import sys
import datetime
import config     ##apikey
import pytz       ##timezone

class Event():
    def __init__(self,date,time,home_team,away_team,
                    home_team_spread,away_team_spread):
        self.date = date
        self.time = time    
        self.home_team = home_team
        self.away_team = away_team
        self.home_team_spread = home_team_spread
        self.away_team_spread = away_team_spread
    def print(self):
        print(self.date)
        print(self.time)
        print(self.home_team)
        print(self.away_team)
        print(self.home_team_spread)
        print(self.away_team_spread)


def get_odds_data_from_api():
    whole_url = 'https://api.the-odds-api.com/v4/sports/basketball_nba/odds/?apiKey='+ config.api_key +'&regions=us&markets=spreads'

    res = requests.get(whole_url)
    return res


def next_game_odds(odds_data_json,team_name,bookie_name='fanduel'):
    
    
    
    
    next_game = [game for game in odds_data_json if game['home_team']==team_name or game['away_team']==team_name ]
    if next_game == []:
        
        print('no next game')
        Next_game_event = Event(' ',' ',' ',' ',' ',' ',)
    else:
        home_team = next_game[0]['home_team']
        away_team = next_game[0]['away_team']
        date = next_game[0]['commence_time'][:10]
        time = next_game[0]['commence_time'][11:]


        
        bookie_data = [entry for entry in next_game[0]['bookmakers'] if entry['key']==bookie_name]
        try:
            team1 = bookie_data[0]['markets'][0]['outcomes'][0]['name']
            team1_spread = bookie_data[0]['markets'][0]['outcomes'][0]['point']
            team2 = bookie_data[0]['markets'][0]['outcomes'][1]['name']
            team2_spread = bookie_data[0]['markets'][0]['outcomes'][1]['point']

            if team1 == home_team:
                home_team_spread = team1_spread
                away_team_spread = team2_spread
            elif team1 == away_team:
                away_team_spread = team1_spread
                home_team_spread = team2_spread 

            Next_game_event = Event(date=date,time=time,home_team=home_team,away_team=away_team,home_team_spread=home_team_spread,away_team_spread=away_team_spread)
        
        except:
            Next_game_event = Event(' ',' ',' ',' ',' ',' ',)

    return Next_game_event




def getActivePlayers():
    player_dict = players.get_players()
    active_players = [player for player in player_dict if player['is_active']==True]
    active_players_names = [x['full_name'] for x in active_players]
    return active_players_names

def getPlayerDict():
    return players.get_players()

def getPlayerCareerStats(player_id_number):
    return playercareerstats.PlayerCareerStats(player_id=str(player_id_number))

def get_player_last10_games(player_id):
    gamelog = playergamelog.PlayerGameLog(player_id=player_id)
    player_last_10_games = gamelog.player_game_log.get_data_frame().iloc[:10]
    return player_last_10_games


def get_player_averages_dict(player_id):
    res = playergamelog.PlayerGameLog(player_id)
    res2 = res.player_game_log.get_data_frame()

    res2_data_only = res2.drop(columns=['WL','MATCHUP','Player_ID','Game_ID','SEASON_ID','VIDEO_AVAILABLE','GAME_DATE','PLUS_MINUS'])

    data_only_averages = [round(res2_data_only[x].mean(),2) for x in res2_data_only.keys()]

    average_dict = {i:j for i,j in zip( res2_data_only.keys(), data_only_averages)}
    
    return average_dict


def get_odds_data():
    
    whole_url = 'https://api.the-odds-api.com/v4/sports/basketball_nba/odds/?apiKey=344f688e5e81f65ba37d33a8b55540a0&regions=us&markets=spreads'

    res = requests.get(whole_url)
    return res

def get_player_current_team(player_id) -> str:
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    career_df = career.get_data_frames()[0]
    if career_df.iloc[-1]['TEAM_ABBREVIATION'] == 'TOT':
        team = career_df.iloc[-2]['TEAM_ABBREVIATION']
    else:
        team = career_df.iloc[-1]['TEAM_ABBREVIATION']
    return str(team)
bookie_abbr_dict={
'DraftKings':       'draftkings',
'Bovada':           'bovada',
'BetUS':            'betus',
'BetMGM':           'betmgm',
'Circa Sports':     'circasports',
'FanDuel':          'fanduel',
'William Hill (US)':'williamhill_us',
'SugarHouse':       'sugarhouse',
'BetRivers':        'betrivers',
'Barstool Sportsbook':'barstool',
'TwinSpires':       'twinspires',
'Unibet':           'unibet_us',
'FOX Bet':          'foxbet',
'PointsBet (US)':   'pointsbetus',
'BetOnline.ag':     'betonlineag',
'LowVig.ag':        'lowvig',
'WynnBET':          'wynnbet',
'SuperBook':        'superbook',
'MyBookie.ag':      'mybookieag',
}


nba_team_dict = {
'ATL': 	'Atlanta Hawks',
'BKN': 	'Brooklyn Nets',
'BOS': 	'Boston Celtics',
'CHA' :	'Charlotte Hornets',
'CHI' :	'Chicago Bulls',
'CLE' :	'Cleveland Cavaliers',
'DAL' :	'Dallas Mavericks',
'DEN' :	'Denver Nuggets',
'DET'	:'Detroit Pistons',
'GSW' 	:'Golden State Warriors',
'HOU'   :'Houston Rockets',
'IND' 	:'Indiana Pacers',
'LAC' 	:'Los Angeles Clippers',
'LAL' 	:'Los Angeles Lakers',
'MEM' 	:'Memphis Grizzlies',
'MIA' 	:'Miami Heat',
'MIL' 	:'Milwaukee Bucks',
'MIN' 	:'Minnesota Timberwolves',
'NOP' 	:'New Orleans Pelicans',
'NYK' 	:'New York Knicks',
'OKC' 	:'Oklahoma City Thunder',
'ORL' 	:'Orlando Magic',
'PHI' 	:'Philadelphia 76ers',
'PHX' 	:'Phoenix Suns',
'POR' 	:'Portland Trail Blazers',
'SAC' 	:'Sacramento Kings',
'SAS' 	:'San Antonio Spurs',
'TOR' 	:'Toronto Raptors',
'UTA' 	:'Utah Jazz',
'WAS' 	:'Washington Wizards'
}


def close_app():
    sys.exit()

##convert time to eastern
def convert_to_datetime(date_string,tzinfo=datetime.timezone.utc):
    date_string = str(date_string)
    year = int(date_string[0:4])
    month = int(date_string[5:7])
    day = int(date_string[8:10])
    hour = int(date_string[11:13])
    minute = int(date_string[14:16])
    second = int(date_string[17:19])
    #print(year,month,day,hour,minute,second)
    datetime_src = datetime.datetime(year,month,day,hour,minute,second)
    
    return datetime_src

def convert_datetime_to_eastern(datetime_src):


    old_timezone = pytz.timezone("UTC")
    new_timezone = pytz.timezone("US/Eastern")
    new_timezone_timestamp = old_timezone.localize(datetime_src).astimezone(new_timezone) 
    return new_timezone_timestamp






def get_one_game_odds_data(odds_data_json,target_team,target_bookie):
    outcomes = []
    next_games = [game for game in odds_data_json if game['home_team']==target_team or game['away_team']==target_team]
    try:
        next_game = next_games[0]
    except:
        print("ERROR: team name error")
    if next_games == []:
        print("No next game")
        game_time=0
        last_update=''
        outcomes=[]
        
    else:
        game_time = next_game['commence_time']
        last_update = next_game['bookmakers'][0]['last_update']
        bookie_all = next_game['bookmakers']
        one_bookie_data = [x for x in bookie_all if x['key']==target_bookie]
        if one_bookie_data==[]:
            print('no data')
        else:
            outcomes = one_bookie_data[0]['markets'][0]['outcomes']
            
    return game_time,last_update,outcomes




def make_odds_api_call(eventid='',keys=[],values=[],apikey=config.api_key):




    url = 'https://api.the-odds-api.com/v4/sports/basketball_nba/events/'
    url += eventid
    url += '/odds?'
    url += 'apiKey='+ apikey + '&'
    for key,value in zip(keys,values):
        url += key
        url += '='
        url += value
        if key!=keys[-1]:
            url += '&'
    
    res = requests.get(url)


    
    return res


## month dictionary
months = {

    'JAN':1,
    'FEB':2,
    'MAR':3,
    'APR':4,
    'MAY':5,
    'JUN':6,
    'JUL':7,
    'AUG':8,
    'SEP':9,
    'OCT':10,
    'NOV':11,
    'DEC':12,
    }

## color dictionaries
colors = {
    'red': QtGui.QColor(255,0,0),
    'green': QtGui.QColor(0,255,0),
    'blue': QtGui.QColor(0,0,255),



    'grad_0':QtGui.QColor(0,168,252),
    'grad_10':QtGui.QColor(108,205,253),
    'grad_20':QtGui.QColor(197,235,254),
    'grad_30':QtGui.QColor(188,150,249),
    'grad_40':QtGui.QColor(179,65,244),
    'grad_50':QtGui.QColor(189,56,211),
    'grad_60':QtGui.QColor(201,46,173),
    'grad_70':QtGui.QColor(213,36,134),
    'grad_80':QtGui.QColor(224,26,98),
    'grad_90':QtGui.QColor(238,14,54),
    'grad_100':QtGui.QColor(255,0,0),













}
