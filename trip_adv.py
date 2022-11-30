import json
import pandas as pd
import kaggle
import os
from kaggle.api.kaggle_api_extended import KaggleApi


current = os.getcwd()


#TODO: Choose dataset to use

api = KaggleApi()
api.authenticate()
api.dataset_download_files('', path=current, unzip=True)


'''
No idea what to do here. We have to determine a dataset first

'''


#converts dataframe to csv
os.system('echo data.csv')

root_df.to_csv('data.csv')

