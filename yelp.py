import json
import pandas as pd
import kaggle
import os
from kaggle.api.kaggle_api_extended import KaggleApi


current = os.getcwd()

print('Downloading dataset...')

api = KaggleApi()
api.authenticate()
api.dataset_download_files('yelp-dataset/yelp-dataset', path=current, unzip=True)

print('Dataset downloaded successfully')

#Lists of the columns wanted from each json file
bus_columns = ['business_id', 'name', 'city', 'stars', 'review_count']
reviews_columns = ['review_id', 'user_id', 'business_id', 'stars', 'date', 'text', 'useful', 'funny', 'cool']
users_columns = ['user_id', 'review_count', 'yelping_since', 'useful', 'funny', 'cool', 'fans', 'elite', 'average_stars']


def add_to_dict(columns, file_path):
    '''
    Function creates pandas dataframe using json file specified in file_path and elements specified in columns

    file_path: Full path (not relative) to json file
    columns: List of column values to extract from json file

    '''

    temp_df = {}                #temporary dictionary that will be turned into dataframe
    data_points = []            

    
    #extracts json dictionary from each value and adds them to data_points array
    for line in open(file_path, "r", encoding = 'cp850'):
       data_points.append(json.loads(line))

    
    #extracts columns specified in columns and adds them to temp_df
    for item in columns:
        temp_df[item] = []
        for point in data_points:
            temp_df[item].append(point[item])
    return pd.DataFrame.from_dict(temp_df)      #returns a pandas dataframe


#joins all dataframes created for each json. Uses .join to join dataframes that are of differnet length

print('Processing dataset...')

root_df = add_to_dict(bus_columns, 'yelp_academic_dataset_business.json')
root_df = pd.merge(root_df, add_to_dict(reviews_columns, 'yelp_academic_dataset_review.json'), on='business_id',  how='outer', suffixes=('_business', '_review'))
root_df = pd.merge(root_df, add_to_dict(users_columns, 'yelp_academic_dataset_user.json'),  on='user_id',  how='outer', suffixes=('_review', '_user'))

print('Processed')
#converts dataframe to csv
os.system('touch data.csv')
print('Converting to csv...')
root_df.to_csv('data.csv')
print('Converted')

