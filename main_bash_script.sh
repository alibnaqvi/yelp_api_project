#!/bin/bash

mkdir temp

mv yelp.py temp

mv trip_adv.py temp

cd temp

git clone #fill in with ML script

python yelp.py

rm data.csv

python trip_adv.py

echo "Running analysis..."

python #fill in with ML script

mv results.csv ..

mv yelp.py ..

mv trip_adv.py ..

cd ..

rm -rf temp

echo "Finished"