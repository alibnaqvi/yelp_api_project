#!/bin/bash

mkdir temp

mv yelp.py temp

cd temp

git clone #fill in with ML script

python yelp.py

echo "Running analysis..."

python #fill in with ML script

mv results.csv ..

mv yelp.py ..

cd ..

rm -rf temp

echo "Finished"