from PyQt5 import QtCore, QtWidgets, QtGui
#from PyQt5.QtWidgets import *

from PyQt5 import uic
import NChelper



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('ui_one.ui', self)



        print('1')

        current_bookie = 'FanDuel'

        self.playerCurrentStatTable.setEnabled(False)
        
        # sets the sportsbook
        self.bookieSelectComboBox.setEnabled(True)
        self.bookieSelectComboBox.addItems(['FanDuel','Barstool'])
        self.bookieSelectComboBox.currentTextChanged.connect(self.bookie_changed)


        #Enable features on 'Start Button' click
        self.start_button.clicked.connect(self.show_app)

        # Populate Active Players
        
        self.select_player_combo_box.addItems(NChelper.getActivePlayers())

        self.player_go_button.clicked.connect(self.showPlayerStats)
        self.quitButton.clicked.connect(self.close_app)

        
## END INIT

    def show_player_next_game(self,player_id):
        self.nextGameInfoTable.setEnabled(True)
        




    def bookie_changed(self, value):
        self.current_bookie = str(value)
        print(self.current_bookie)

    def showPlayerStats(self):
        #gets name selected in pull down menu
        player_name = self.select_player_combo_box.currentText()
        print(player_name)
        # gets ID of that player
        id_ = [player for player in NChelper.getPlayerDict() if player['full_name']==player_name][0]['id']
        print(id_)





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


        #clear table
        for i in range(len(career_stats.iloc[-1].keys())):
            self.playerCurrentStatTable.setItem(0,i, QtWidgets.QTableWidgetItem(''))
            self.playerCurrentStatTable.setItem(1,i, QtWidgets.QTableWidgetItem(''))
            self.playerCurrentStatTable.item(0, i).setBackground(QtGui.QColor(255,255,255))
            self.playerCurrentStatTable.item(1, i).setBackground(QtGui.QColor(255,255,255))


        #headers for table
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
                self.last10gamestable.setItem(j,i, QtWidgets.QTableWidgetItem(str(last10_rev_short.iloc[j][i])))
        


        

        self.last10gamestable.resizeRowsToContents()
        self.last10gamestable.resizeColumnsToContents()

        ## Get Next Game 
        player_team_short = NChelper.get_player_current_team(id_)
        print(player_team_short)
        
        assert player_team_short != 'TOT', 'team short name cant be TOT'
        full_team_name = NChelper.nba_team_dict[player_team_short]



    def show_app(self):
        self.player_title_label.setEnabled(True)
        self.select_player_combo_box.setEnabled(True)
        self.player_go_button.setEnabled(True)
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