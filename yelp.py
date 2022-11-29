import json
import pandas as pd
import kaggle
import os

#TODO: figure out this kaggle api 

current = os.getcwd()

kaggle.api.authenticate()
kaggle.api.dataset_download_files('Yelp Dataset', path=current, unzip=True)

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

#TODO: Change '\\temp' to the name of kaggle dataset file

root_df = add_to_dict(bus_columns, current + '\\temp' + '\yelp_academic_dataset_business.json')
root_df = root_df.join(add_to_dict(reviews_columns, current + '\\temp' + '\yelp_dataset\yelp_academic_dataset_review.json'), lsuffix='_business', rsuffix='_review')
root_df = root_df.join(add_to_dict(users_columns, current + '\\temp' + '\yelp_academic_dataset_user.json'), lsuffix='_review', rsuffix='_user')

#converts dataframe to csv
root_df.to_csv('everything.csv')

