#!/bin/bash

git clone #fill in with ML script

mv yelp.py #name of git folder

cd #name of git folder

python yelp.py

echo "Running analysis..."

python #fill in with ML script

mv results.csv ..

mv yelp.py ..

rm -rf .git

cd ..

rm -rf #name of git folder

echo "Finished"