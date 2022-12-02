#!/bin/bash

git clone https://github.com/m-yen/Applying-PageRank-to-Resturant-Reviews

mv yelp.py Applying-PageRank-to-Resturant-Reviews

cd Applying-PageRank-to-Resturant-Reviews

python yelp.py

echo "Running analysis..."

jupyter nbconvert --to script 'final_review_algorithm_1_1.ipynb'

mv final_review_algorithm_1_1.txt final_review_algorithm_1_1.py

python final_review_algorithm_1_1.py


mv results.csv ..

mv yelp.py ..

rm -rf .git

cd ..

rm -rf Applying-PageRank-to-Resturant-Reviews

echo "Finished"