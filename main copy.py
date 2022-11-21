import json

tweet = []

for line in open("/Users/alinaqvi/Desktop/SWE/yelp_dataset/yelp_academic_dataset_business.json", "r"):
    tweet.append(json.loads(line))

print(tweet[0])