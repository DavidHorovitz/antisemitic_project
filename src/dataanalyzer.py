import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame


class DataAnalyzer:
    def __init__(self,table: DataFrame):
        self.df=table
        '''
        Agreed how many of each category there are
        '''
    def sum_of_category(self):
        print(self.df['Biased'].value_counts())
        print(f"{self.df['Biased'].value_counts().sum()}")
        '''
        Average of categories
        '''
    def Average_len_of_category(self):
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
        '''
        3 longest in each category
        '''
        def longest_text():
            tweets_dict_antisemit = {}
            tweets_dict_no_antisemit = {}
            for i in range(0, len(self.df['Text']) - 1):
                if self.df['Biased'][i] == 1:
                    # len_of_antisemit= len(df['Text'][i].split(" "))
                    len_of_antisemit = len(self.df['Text'][i])
                    tweets_dict_antisemit[self.df['Text'][i]] = len_of_antisemit
                else:
                    len_of_no_antisemit = len(self.df['Text'][i])
                    tweets_dict_no_antisemit[self.df['Text'][i]] = len_of_no_antisemit

            arr_of_antisemit = []
            arr_of_no_antisemit = []
            for j in range(3):
                maxy = max(tweets_dict_antisemit.values())
                print(max(tweets_dict_antisemit.values()))
                for key, valeu in tweets_dict_antisemit.items():
                    if valeu == maxy:
                        arr_of_antisemit.append(key)
                        tweets_dict_antisemit[key] = 0
            for k in range(3):
                maxy = max(tweets_dict_no_antisemit.values())
                print(max(tweets_dict_antisemit.values()))
                for key, valeu in tweets_dict_no_antisemit.items():
                    if valeu == maxy:
                        arr_of_no_antisemit.append(key)
                        tweets_dict_no_antisemit[key] = 0
            for j in range(3):
                maxy = max(tweets_dict_antisemit.values())
                for key, valeu in tweets_dict_antisemit.items():
                    if valeu == maxy:
                        arr_of_no_antisemit.append(key)
                        tweets_dict_antisemit[key] = 0
            for text in arr_of_antisemit:
                print("ANTISEMIT!", text)
            for text in arr_of_no_antisemit:
                print("NO ANTISEMIT!", text)


