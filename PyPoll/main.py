# Dependencies
import os
import csv

# Load csv file
file_path = os.path.join("PyPoll", "Resources", "election_data.csv.")

with open(file_path) as csvfile:
    election_data = csv.reader(csvfile, delimiter=",")
    # store the headers in a seperate variable
    headings = next(election_data)
    
    # Set counter
    total_votes = 0
    candidate_list = []
    candidate_vote = {}

    for row in election_data:
        total_votes += 1
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            candidate_vote[row[2]] = 1
        else:
            candidate_vote[row[2]] += 1
    
    # Calculate percentage
    candidate_1 = round(candidate_vote["Charles Casper Stockham"] / total_votes *100, 3)
    candidate_2 = round(candidate_vote["Diana DeGette"] / total_votes *100, 3)
    candidate_3 = round(candidate_vote["Raymon Anthony Doane"] / total_votes *100, 3)

    # Find the winner
    # compile each candicate's vote count into a list
    vote_list = [candidate_vote["Charles Casper Stockham"], candidate_vote["Diana DeGette"], candidate_vote["Raymon Anthony Doane"]]

    # find the winner's name with the highest number of votes received
    for key in candidate_vote:
        if candidate_vote[key] == max(vote_list):
            winner_name = key

    # print analysis statements
    print("Election Results \n-------------------------")
    print(f"Total Month: {total_votes}\n-------------------------")
    print(f"{candidate_list[0]}: {candidate_1}% (" + str(candidate_vote[candidate_list[0]]) + ")")
    print(f"{candidate_list[1]}: {candidate_2}% (" + str(candidate_vote[candidate_list[1]]) + ")")
    print(f"{candidate_list[2]}: {candidate_2}% (" + str(candidate_vote[candidate_list[2]]) + ")")
    print(f"-------------------------\nWinner: {winner_name}\n-------------------------")
    
    # export the results as a text file
    output_path = os.path.join("PyPoll", "analysis", "Election_analysis_results.txt")
    lines = ["Election Results \n-------------------------",
    f"Total Month: {total_votes}\n-------------------------",
    f"{candidate_list[0]}: {candidate_1}% (" + str(candidate_vote[candidate_list[0]]) + ")",
    f"{candidate_list[1]}: {candidate_2}% (" + str(candidate_vote[candidate_list[1]]) + ")",
    f"{candidate_list[2]}: {candidate_2}% (" + str(candidate_vote[candidate_list[2]]) + ")",
    f"-------------------------\nWinner: {winner_name}\n-------------------------"]
   
    with open(output_path, 'w') as f:
        for l in lines:
            f.write(l)
            f.write("\n")
