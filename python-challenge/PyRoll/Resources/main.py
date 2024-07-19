import os
import csv

# Path to the election data CSV file
file_path = "election_data.csv"

# Initialize variables to store as counters
total_votes = 0
candidates = {}
winner = {"name": "", "votes": 0}

# Read and open the CSV file, skipping the header to go to the next line 
with open(file_path, mode="r") as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader) 

# Here, you can extract candidate name from the row
    for row in csv_reader:
        candidate = row[2]

        # Increment the total number of votes
        total_votes += 1

        # If the candidate is not in the dictionary, add them with 0 votes
        if candidate not in candidates:
            candidates[candidate] = 0

        # Incrementally add the candidate's vote count
        candidates[candidate] += 1

        # This will update the winner if the current candidate has more votes
        if candidates[candidate] > winner["votes"]:
            winner["name"] = candidate
            winner["votes"] = candidates[candidate]

# Prepare the analysis report
report = (
    "Election Results\n"
    "--------------------------\n"
    f"Total Votes: {total_votes}\n"
    "--------------------------\n"
)

# Add each candidate's results to the report
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100

# The {percentage:.3f}% allows us to more accurately return the percentage of votes up to three decimals
    report += f"{candidate}: {percentage:.3f}% ({votes})\n"

# This allows us to append the winner to the end of the report
report += (
    "--------------------------\n"
    f"Winner: {winner['name']}\n"
    "--------------------------\n"
)

print(report)

# Export the results to a text file
with open('election_results.txt', mode='w') as file:
    file.write(report)