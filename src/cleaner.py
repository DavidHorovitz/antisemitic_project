from pandas import DataFrame
import pandas as pd

class Cleaner:
    def __init__(self,table: DataFrame):
        self.df = table
        self.new_df=""
    '''
     Creates a new dataframe
    '''
    def new_df(self):
        self.new_df=self.df[['Text','Biased']]
        return self.new_df

    def replaiser(self):
        self.new_df['Text'] = self.new_df['Text'].str.replace(",", " ")
        return self.new_df

    def convert_tu_lower(self):
        self.new_df['Text']=self.new_df['Text'].str.lower()
        return self.new_df
    def drop_nul(self):
        cleaned_df = self.new_df.dropna()
        return cleaned_df
