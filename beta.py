from PyQt5 import QtCore, QtWidgets, QtGui
#from PyQt5.QtWidgets import *

from PyQt5 import uic
import NChelper
import logging


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('ui_one.ui', self)

        logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


        logging.info('Program Start')
        

        current_bookie = 'FanDuel'

        self.playerCurrentStatTable.setEnabled(False)
        
        # sets the sportsbook
        self.bookieSelectComboBox.setEnabled(True)
        self.bookieSelectComboBox.addItems(['FanDuel','Barstool'])
        self.bookieSelectComboBox.currentTextChanged.connect(self.bookie_changed)
        self.current_bookie = self.bookieSelectComboBox.currentText()
        self.current_bookie = NChelper.bookie_abbr_dict[self.current_bookie]

        #Enable features on 'Start Button' click
        self.start_button.clicked.connect(self.show_app)

        # Populate Active Players
        
        self.select_player_combo_box.addItems(NChelper.getActivePlayers())

        self.player_go_button.clicked.connect(self.showPlayerStats)
        self.quitButton.clicked.connect(self.close_app)


        self.odds_data = NChelper.get_odds_data_from_api()

        ## populate TEAMS select box

        self.teamSelectComboBox.addItems(NChelper.nba_team_dict.values())
        self.teamSelectComboBox.currentTextChanged.connect(self.teamBox_changed)
        self.current_team_selection = self.teamSelectComboBox.currentText()
        
        

        print(self.current_team_selection)
        
        






        
## END INIT

    def teamBox_changed(self, value):
        '''
        triggered by changing TEAM combo box

        also clears playerfromteam combo box
        '''
        self.teamBoxSelection = str(value)
        self.playerFromTeamComboBox.clear()
        logging.info("teambox changed:"+str(value))

        self.playerFromTeamComboBox.addItems(['1','2','3'])
        





    def show_player_next_game(self,player_id):
        self.nextGameInfoTable.setEnabled(True)
        




    def bookie_changed(self, value):
        self.current_bookie = str(value)
        logging.info("bookie changed to" + str(value))

    def showPlayerStats(self):
        """
        
        
        Called when 'get stats' UI button is pressed by user

        Clears Main Info Table
        Clears Next Game Table

        """
        #gets name selected in pull down menu
        player_name = self.select_player_combo_box.currentText()
        logging.info('player: %s', player_name)

        # gets ID of that player
        id_ = [player for player in NChelper.getPlayerDict() if player['full_name']==player_name][0]['id']
        logging.info('id: %s', id_)
        





        self.playerCurrentStatTable.setEnabled(True)
        career_stats = NChelper.getPlayerCareerStats(id_).get_data_frames()[0]

        try:
            career_stats = career_stats.drop(columns=['LEAGUE_ID','PLAYER_ID','SEASON_ID','TEAM_ID'])
        except:
            print('error')

        career_stats.rename(columns={"TEAM_ABBREVIATION": "TEAM"}, inplace=True)
        career_stats.rename(columns={"PLAYER_AGE": "AGE"}, inplace=True)


        self.playerCurrentStatTable.setRowCount(2)
        self.playerCurrentStatTable.setColumnCount(len(career_stats.iloc[-1].keys()))


        #clear player stat table
        for i in range(len(career_stats.iloc[-1].keys())):
            self.playerCurrentStatTable.setItem(0,i, QtWidgets.QTableWidgetItem(''))
            self.playerCurrentStatTable.setItem(1,i, QtWidgets.QTableWidgetItem(''))
            self.playerCurrentStatTable.item(0, i).setBackground(QtGui.QColor(255,255,255))
            self.playerCurrentStatTable.item(1, i).setBackground(QtGui.QColor(255,255,255))


        #headers for player stat table
        self.playerCurrentStatTable.setHorizontalHeaderLabels(career_stats.iloc[-1].keys())

        #get averages (over season)
        player_averages_dict = NChelper.get_player_averages_dict(id_)


        # puts data in the table locations
        for i in range(len(career_stats.iloc[-1].keys())):
            self.playerCurrentStatTable.setItem(0,i, QtWidgets.QTableWidgetItem(str(career_stats.iloc[-1][i])))
            if career_stats.iloc[-1].keys()[i] in player_averages_dict.keys():
                self.playerCurrentStatTable.setItem(1,i, QtWidgets.QTableWidgetItem(str(player_averages_dict[career_stats.iloc[-1].keys()[i]])))


        self.playerCurrentStatTable.setItem(1,2, QtWidgets.QTableWidgetItem('Averages:'))

        



        self.playerCurrentStatTable.resizeRowsToContents()
        self.playerCurrentStatTable.resizeColumnsToContents()


        ## Last 10 games Table

        last_10_games = NChelper.get_player_last10_games(id_)
        last10_rev = last_10_games.iloc[::-1]
        last10_rev_short = last10_rev.drop(columns=['SEASON_ID','Player_ID','Game_ID','OREB','DREB','TOV','PF','PLUS_MINUS','VIDEO_AVAILABLE','FTM','FTA','FT_PCT','STL','BLK'])


        self.last10gamestable.setRowCount(10)
        self.last10gamestable.setColumnCount(len(last10_rev_short.keys()))


        #clear table
        self.last10gamestable.setEnabled(True)

        for i in range(len(last10_rev_short.keys())):
            for j in range(9):
                self.last10gamestable.setItem(j,i, QtWidgets.QTableWidgetItem(''))
                self.last10gamestable.item(j, i).setBackground(QtGui.QColor(255,255,255))

        self.last10gamestable.setHorizontalHeaderLabels(last10_rev_short.keys())



        # puts data in the table locations
        for i in range(len(last10_rev_short.keys())):
            for j in range(10):
                try:
                    self.last10gamestable.setItem(j,i, QtWidgets.QTableWidgetItem(str(last10_rev_short.iloc[j][i])))
                except:
                    pass
        print(str(last10_rev_short.iloc[0][0]))
        print(str(last10_rev_short.iloc[1][0]))
        print(last10_rev_short['GAME_DATE'])


        ## colors GAME_DATE if more than 14 days ago
        for i in range(len(last10_rev_short['GAME_DATE'])):
            date_string = last10_rev_short.iloc[i][0]
            month_abbr = date_string[0:3]
            month = NChelper.months[month_abbr]
            day = date_string[4:6]
            year = date_string[8:12]
            date = NChelper.datetime.date(int(year),int(month),int(day))
            today = NChelper.datetime.date.today()
            days_since = today-date
            print(days_since.days)
            if days_since.days > 14:
                self.last10gamestable.item(i, 0).setBackground(NChelper.colors['red'])




        self.last10gamestable.resizeRowsToContents()
        self.last10gamestable.resizeColumnsToContents()


        ## table items must be populated before you can set background color

        ##  get all stats for player for whole season

        ##  for each attribute, get 10s percentile values


        ## color code stat cells based on value
        self.last10gamestable.item(3, 5).setBackground(QtGui.QColor(100,100,150))




        ### START Next Game Table

        ## get player's current team from current year stats
        player_team_short = NChelper.get_player_current_team(id_)
        
        #print(player_team_short)
        
        # if player was traded this year, last entry in table will show TOT
        #    for total, get team name from previous row
        assert player_team_short != 'TOT', 'team short name cant be TOT'
        full_team_name = NChelper.nba_team_dict[player_team_short]
        ##Have player ID, name, team name

        ## get next game info
        ## info == date, time, hometeam, away team, spreads

        
        ## get odds Json, from odds data loaded on start
        odds_data_json = self.odds_data.json()
        ## helper function will return next game info:
        ###     hometeam, awayteam, spreads, date, time
        
        self.nextGameInfoTable.setEnabled(True)

        self.nextGameInfoTable.setRowCount(2)
        self.nextGameInfoTable.setColumnCount(5)

        #headers for table
        self.nextGameInfoTable.setHorizontalHeaderLabels(["Next Game","Last Update","Team","Price","Spread"])
        #Clear Table contents
        self.nextGameInfoTable.clearContents()
        self.nextGameInfoTable.setVerticalHeaderLabels([])

        print(self.current_bookie)
        next_game_time,last_update,bet_info = NChelper.get_one_game_odds_data(odds_data_json=odds_data_json,target_team=full_team_name,target_bookie=self.current_bookie)
        logging.info("next game:" + str(next_game_time))
        if bet_info!=[]:
        
            next_game_time_GMT = NChelper.convert_to_datetime(next_game_time)
            last_update_GMT = NChelper.convert_to_datetime(last_update)
            next_game_time_EST = NChelper.convert_datetime_to_eastern(next_game_time_GMT)
            last_update_EST = NChelper.convert_datetime_to_eastern(last_update_GMT)
            
        



            self.nextGameInfoTable.setItem(0,0,QtWidgets.QTableWidgetItem(next_game_time_EST.strftime("%Y  %b %d  %I:%M %p  %Z")))
            self.nextGameInfoTable.setItem(0,1,QtWidgets.QTableWidgetItem(last_update_EST.strftime("%Y  %b %d  %I:%M %p  %Z")))

        if bet_info==[]:
            for i in range(3):
                self.nextGameInfoTable.setItem(0,2+i,QtWidgets.QTableWidgetItem('no data'))
                self.nextGameInfoTable.setItem(1,2+i,QtWidgets.QTableWidgetItem('no data'))
        else:   
            for row,item in enumerate(bet_info):
                self.nextGameInfoTable.setItem(row,2,QtWidgets.QTableWidgetItem(str(item['name'])))
                self.nextGameInfoTable.setItem(row,3,QtWidgets.QTableWidgetItem(str(item['price'])))
                self.nextGameInfoTable.setItem(row,4,QtWidgets.QTableWidgetItem(str(item['point'])))

            
            






        self.nextGameInfoTable.resizeRowsToContents()
        self.nextGameInfoTable.resizeColumnsToContents()
        ## END Next Game Table




    def show_app(self):
        
        self.player_title_label.setEnabled(True)
        self.select_player_combo_box.setEnabled(True)
        self.player_go_button.setEnabled(True)
        self.teamSelectComboBox.setEnabled(True)
        self.playerFromTeamComboBox.setEnabled(True)
        return
    


    def close_app(self):
        NChelper.close_app()
   







def main():
    import sys
    app = QtWidgets.QApplication([])


    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())





if __name__ == '__main__':
    main()