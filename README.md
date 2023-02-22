# Yelp True Review Project


## General info
This project is designed to serve as a simple pipeline to acquire our team's data. It allows users to pull our script and gain our analysis with a single command. The analysis is found at another repo: https://github.com/m-yen/Applying-PageRank-to-Resturant-Reviews

The analysis aims to define a more accurate review metric for the Yelp dataset using markov chains, similar to Google's pagerank. We hope to expand this project by accepting using input to provide data for particular resturants rather than returning all resturant values, essentially adding a search feature.






## Technologies
This project pulls the Yelp dataset from Kaggle and runs analyses on it. It does this using the Kaggle API and a Bash script. It uses jupyter notebook and nbconvert to run python files that conduct the analyses. It returns a csv file, and takes a while to run. Be prepared to wait 15 minutes or more, since the program is downloading, unzipping, and processing 10gb of data. 







## Setup
To run this project, you need to have the Kaggle API set up on your system. You also need to have jupyter notebook and nbconvert installed. Other dependencies are managed by the script. Furthermore, downloaded files are deleted upon completion, so all that the user will see is this repo's clone and an output file. It goes without saying that Git needs to be installed. 
