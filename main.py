import json
#import pandas as pd

val_of_int = ['business_id','name']

businesses = []
middle = {}

for line in open("/Users/alinaqvi/Desktop/SWE/yelp_dataset/yelp_academic_dataset_business.json", "r"):
    businesses.append(json.loads(line))

for item in val_of_int:
    middle[item] = {}
    for business in businesses:
        middle[item][business['business_id']] = business[item]

#df = pd.read_json(middle)
#df.to_csv('/Users/alinaqvi/Desktop/SWE/everything.csv')

print(middle)
