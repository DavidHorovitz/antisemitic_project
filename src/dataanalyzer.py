import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame
from pandas.plotting import table

from loader import Loader as lo
class DataAnalyzer:
    def __init__(self,table: DataFrame):
        self.df=table
    def sum_of_category(self):
        print(self.df['Biased'].value_counts())
        print(f"{self.df['Biased'].value_counts().sum()}")

    def len_of_category(self):
        antisemit = 0
        count_of_antisemit = 0
        no_antisemit = 0
        count_of_no_antisemit = 0
        for i in range(0, len(self.df['Text']) - 1):
            if self.df['Biased'][i] == 1:
                antisemit += len(self.df['Text'][i].split(" "))
                count_of_antisemit += 1
            else:
                no_antisemit += len(self.df['Text'][i].split(" "))
                count_of_no_antisemit += 1

        print("antisemit:", antisemit / count_of_antisemit)
        print("no_antisemit:", no_antisemit / count_of_no_antisemit)
        print((antisemit + no_antisemit) / (count_of_antisemit + count_of_no_antisemit))



