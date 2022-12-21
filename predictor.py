import pandas as pd
import numpy as np

class Model():
    def clean(df):
        '''
        (dataframe) -> dataframe
        Takes the dataframe form of a CSV file and returns a dataframe with specified columns removed
        '''
        
        # drops unnecessary columns
        drop_cols = ['Team','Against','Home','ORB','DRB','+/-','GameLink']
        return df.drop(drop_cols, inplace=False, axis=1)

    def get_player_stats(df, name):
        # gets rows with player name and drops all the other rows
        return df.where(df['Player'] == name).dropna(how='all')

    def get_player_names(df):
        # gets all the unique names of players
        df.drop_duplicates(subset=['Player'], inplace=True)
        return np.array(df['Player'])

    if __name__ == '__main__':
        df = pd.read_csv('datasets/2018-19.csv')
        df.cleaned = clean(df)
        test = get_player_stats(df.cleaned, 'Bradley Beal')

        print(get_player_names(df.cleaned))