'''
    Goal: output analysis that calculates:
    The total number of votes cast

    A complete list of candidates who received votes

    The percentage of votes each candidate won

    The total number of votes each candidate won

    The winner of the election based on popular vote

'''


import csv

import os

election_csv=os.path.join("Resources", "election_data.csv")

output_txt = os.path.join("..","Analysis", "election_results.txt")

totalVotes = 0
candidates = []
candOptions = {}

# open csv file
with open(election_csv) as elections:
    
    # csv file reader
    csvReader = csv.reader(elections, delimiter=",")

    # skip header
    next(elections)

    for row in csvReader:
        # add 1 to the total votes as the loop runs
        totalVotes += 1

        # set the candidate name to the current index 2 (Candidate) value
        candidate_name =row[2]
        if candidate_name not in candidates:
            
            candidates.append(candidate_name)
            candOptions[candidates]
        else:
            candOptions[candidates] += 1



