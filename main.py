import csv
import os

# List to store data
candidates = []
winner_value = 0

# Path to the election results
election_result1_CSV = os.path.join("PyPoll","raw_data","election_data_1.csv")
election_result2_CSV = os.path.join("PyPoll","raw_data","election_data_2.csv")

# Path to output file
result_output = os.path.join("PyPoll","election_results.txt")

# Read in the first election results file
with open(election_result1_CSV, newline='') as election_result_file1:
    election_result1 = csv.reader(election_result_file1, delimiter=',')
    
    # Skip the first row to the csv
    next(election_result1, None)
    
    # Loop through rows
    for row in election_result1:
        # Add election result to candidates list
        candidates.append(row[2])

# Read in the second election results file
with open(election_result2_CSV, "r") as election_result_file2:
    election_result2 = csv.reader(election_result_file2, delimiter=',')
    
    # Skip the first row to the csv
    next(election_result2, None)
    
    # Loop through rows
    for row in election_result2:
        # Add election result to candidates list
        candidates.append(row[2])    
        
with open(result_output, "w") as text_file:

    # Calculate the total votes cast
    total_votes = len(candidates)
 

    count = dict((x, candidates.count(x)) for x in set(candidates))
    # Print to terminal
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(total_votes))
    print("-------------------------")
    # Print to textfile
    print("Election Results", file = text_file)
    print("-------------------------", file = text_file)
    print("Total Votes: " + str(total_votes), file = text_file)
    print("-------------------------", file = text_file)

    # Iterate through the count dictionary
    for key, value in count.items():
        # Print the percent and amount of votes each candidate got to terminal
        print(str(key) + ": " + str(round(value/total_votes*100,2)) + "% (" + str(value) + ")")
        # Print the percent and amount of votes each candidate got to textfile
        print(str(key) + ": " + str(round(value/total_votes*100,2)) + "% (" + str(value) + ")", file = text_file)
        # Find the winner
        if value > winner_value:
            winner_value = value
            winner = key
    # Print winner to terminal
    print("-------------------------")    
    print("Winner: " + str(winner))
    # Print winner to textfile
    print("-------------------------", file = text_file)    
    print("Winner: " + str(winner), file = text_file)