from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import playergamelog
import requests
import sys

def get_odds_data_from_api():
    whole_url = 'https://api.the-odds-api.com/v4/sports/basketball_nba/odds/?apiKey=344f688e5e81f65ba37d33a8b55540a0&regions=us&markets=spreads'

    res = requests.get(whole_url)
    return res


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
