#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote

import os
import csv

# Define csv path
election_data_csv = os.path.join("Resources", "election_data.csv")

# Initialize Variables
total_votes_cast = 0
winning_vote = 0
candidates_list = {}
winner = ""
results = []

# Read the csv file
with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #Skip header
    header = next(csvreader)

    for row in csvreader:
        # Extract row data
        voter_id = row[0]
        county = row[1]
        candidate = row[2]

        # Determine total number of votes
        total_votes_cast +=1

        # Determine number of votes for each candidate
        if candidate in candidates_list:
        	candidates_list[candidate] += 1
        else:
        	candidates_list[candidate] = 1

# Prepare total votes results
results.append("Election Results")
results.append("---------------------------")
results.append(f"Total Votes: {total_votes_cast}")
results.append("---------------------------")   

# Calculate percentages
for candidate, votes in candidates_list.items():
	percentage = (votes / total_votes_cast) * 100

	# Prepare % result
	results.append(f"{candidate}: {percentage:.3f}% ({votes})")

	# Find winner
	if votes > winning_vote:
		winner = candidate
		winning_vote = votes

# Prepare winner results
results.append("---------------------------")
results.append(f"Winner: {winner}")
results.append("---------------------------")

#Print Results in terminal
for line in results:
	print(line)

# Output as txt file
output_directory = r"C:\Users\bfletchall\Desktop\Challenge_repos\python-challenge\PyPoll\Analysis\Election_Data_Results.txt"
with open(output_directory, "w") as txtfile:
	for line in results:
		txtfile.write(line + "\n")		