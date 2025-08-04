from pprint import pprint

import pandas as pd


class Loader:

    def loader(self):
        df = pd.read_csv("tweets_dataset.csv")
        return df
















        # print(df['Text'].value_counts().mean(len(df.split)))
        # ss.split(" ")
        # print(len(ss))

        # return df



a=Loader()
a.loader()