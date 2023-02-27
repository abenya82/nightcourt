from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import playergamelog
import requests
import sys

import config

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
