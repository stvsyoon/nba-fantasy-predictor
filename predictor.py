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
        drop_cols = ['rm','ORB','DRB','+/-']
        return self.df.drop(drop_cols, inplace=True, axis=1)

    def get_player_stats(self, name):
        # gets rows with player name and drops all the other rows
        self.df[self.df['FG'].str.contains('Did Not Play')==False]
        return self.df.where(self.df['Player'] == name).dropna(how='all')

    def get_player_names(self):
        # gets all the unique names of players
        self.df.drop_duplicates(subset=['Player'], inplace=True)
        return np.array(df['Player'])
    
    def get_season_average(self, name):
        df = self.get_player_stats(name)
        return df.median()
        

df = pd.read_csv('datasets/nba.csv')
m = Data(df)
m.clean()
test = m.get_player_stats('James Harden')
print(test)
# print(m.get_season_average('Bradley Beal'))


