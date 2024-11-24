# -*- coding: UTF-8 -*- 
"""PyPoll Homework Solution."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candi_option = []
candi_votes = {}

# Winning Candidate and Winning Count Tracker
winning_votes = 0
winning_candidate = ""

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row (assuming it's in column 3)
        candi_name = row[2]

        # If the candidate is not already in the candidate list, add them
        # else, add a vote to the candidate's count
        if candi_name not in candi_option:
            candi_option.append(candi_name)
            candi_votes[candi_name] = 1  # Start their vote count at 1
        else:
            candi_votes[candi_name] += 1  # Add a vote to the candidate

# Print and save the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Open a text file to save the output
with open(file_to_output, "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candi_votes:
        candidate_votes = candi_votes[candidate]
        candidate_percentage = (candidate_votes / total_votes) * 100

        # Update the winning candidate if this one has more votes
        if candidate_votes > winning_votes:
            winning_votes = candidate_votes
            winning_candidate = candidate

        # Print each candidate's vote count and percentage
        print(f"{candidate}: {candidate_percentage:.3f}% ({candidate_votes})")
        # Save each candidate's vote count and percentage to the text file
        output_file.write(f"{candidate}: {candidate_percentage:.3f}% ({candidate_votes})\n")

    # Print the winning candidate summary
    print("-------------------------")
    print(f"Winner: {winning_candidate}")
    print("-------------------------")

    # Save the winning candidate summary to the text file
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winning_candidate}\n")
    output_file.write("-------------------------\n")
