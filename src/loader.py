from pprint import pprint

import pandas as pd


class Loader:
    def loader(self):
        df = pd.read_csv("tweets_dataset.csv")
        # return df
        tweets_dict_antisemit={}
        tweets_dict_no_antisemit={}
        for i in range(0, len(df['Text']) - 1):
            if df['Biased'][i] == 1:
                # len_of_antisemit= len(df['Text'][i].split(" "))
                len_of_antisemit= len(df['Text'][i])
                tweets_dict_antisemit[df['Text'][i]] = len_of_antisemit


            else:
                len_of_no_antisemit = len(df['Text'][i])
                tweets_dict_no_antisemit[df['Text'][i]] = len_of_no_antisemit



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
















        # print(df['Text'].value_counts().mean(len(df.split)))
        # ss.split(" ")
        # print(len(ss))

        # return df



a=Loader()
a.loader()