'''
    Goal: output analysis that calculates:
    The total number of votes cast

    A complete list of candidates who received votes

    The percentage of votes each candidate won

    The total number of votes each candidate won

    The winner of the election based on popular vote

'''

# import modules
import csv

import os
# csv file path
election_csv=os.path.join("Resources", "election_data.csv")
# output file path
output_txt = os.path.join("..","Analysis", "electionAnalysis.txt")
# set variable, list, and dictionary
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
        candidateName =row[2]
        if candidateName not in candidates:
            # add candidate_name to the candidate list
            candidates.append(candidateName)
            # add the name to the candidate dictionary and set equal to one to count
            # the vote
            candOptions[candidateName] = 1
        else:
            # add on 1 to the a candidates total
            candOptions[candidateName] += 1

# output analysis to terminal
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {totalVotes}")
print(f"-------------------------")

# find the winner
# 
winner = ""  
winnerTotal = 0
# loop through candOptions dictionary to get candidate names and total votes for each
for candidateName, votes in candOptions.items():
    # calculate vote percentage for each candidate, dividing their vote total
    # by the total votes
    votePercentage = round(votes / totalVotes * 100, 3)
    # print each candidate, percentage, and vote total as it loops
    print(f"{candidateName}: {votePercentage}% ({votes})")
    
    #if votes > candOptions[2]:
        #winnerTotal = votes
        #winner = candidateName
    
print(f"-------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")

# write to electionAnalysis.txt file and output to Analysis
with open (output_txt, "w") as outputTxt:
    outputTxt.write(f"Election Results\n")
    outputTxt.write(f"-------------------------\n")
    outputTxt.write(f"Total Votes: {totalVotes}\n")
    outputTxt.write(f"-------------------------\n")
    for candidateName, votes in candOptions.items():
       votePercentage = round(votes / totalVotes * 100, 3)
       outputTxt.write(f"{candidateName}: {votePercentage}% ({votes})\n")
    outputTxt.write(f"-------------------------\n")
    outputTxt.write(f"Winner: {winner}\n")
    outputTxt.write(f"-------------------------\n")
