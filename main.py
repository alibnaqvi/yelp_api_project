import json
import pandas as pd

val_of_int = ['name', 'business_id']

businesses = []
middle = {}

for line in open(R"D:\UC Berkeley\CS Stuff\yeSWEcan\yeSWEcan Final Project\yelp_dataset\yelp_academic_dataset_business.json", "r", encoding = 'cp850'):
    businesses.append(json.loads(line))

for item in val_of_int:
    middle[item] = []
    for business in businesses:
        middle[item].append(business[item])

df = pd.DataFrame.from_dict(middle)
df.to_csv('everything.csv')

