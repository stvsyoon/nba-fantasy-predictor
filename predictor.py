import pandas as pd
import numpy as np

class Model():
    def clean(df):
        '''
        (dataframe) -> dataframe
        Takes the dataframe form of a CSV file and returns a dataframe with specified columns removed
        '''
        

        # drops unnecessary columns
        drop_cols = ['Date','Team','Against','Home','ORB','DRB','+/-','GameLink']
        df.drop(drop_cols, inplace=True, axis=1)

        # group by players and their stat averages
        final = df.groupby('Player').mean()

        return final


    if __name__ == '__main__':
        df = pd.read_csv('datasets/2019-20.csv')
        df.cleaned = clean(df)
        print(df.cleaned.head())