import pandas as pd
import numpy as np

class Data:
    def __init__(self, df):
        self.df = df

    def clean(self):
        '''
        (dataframe) -> dataframe
        Takes the dataframe form of a CSV file and returns a dataframe with specified columns removed
        '''
        
        # drops unnecessary columns
        drop_cols = ['Date','Team','Against','Home','ORB','DRB','+/-','GameLink']
        return self.df.drop(drop_cols, inplace=True, axis=1)

    def get_player_stats(self, name):
        # gets rows with player name and drops all the other rows
        return self.df.where(self.df['Player'] == name).dropna(how='all')

    def get_player_names(self):
        # gets all the unique names of players
        self.df.drop_duplicates(subset=['Player'], inplace=True)
        return np.array(df['Player'])
    
    def get_season_average(self, name):
        df = self.get_player_stats(name)
        return df.mean()



df = pd.read_csv('datasets/2018-19.csv')
m = Data(df)
m.clean()
test = m.get_player_stats('Bradley Beal')
# print(m.get_season_average('Bradley Beal'))


