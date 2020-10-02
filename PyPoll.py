# The data we need to retrieve.
# 1. The total number of votes cast 
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add dependencies
import os
import csv

# Assign variable for the file to load with the path
file_to_load = os.path.join('Resources','election_results.csv')
# Create a filename variable to a direct or indirect path to the save file
file_to_save = os.path.join('Analysis', 'election_analysis.txt')

# Initialize the counter variable for total votes, candidate names, candidate votes, vote percentage, candidate results
# winning candidate, winning vote count, and winning vote percentage
total_votes = 0
candidate_options = []
candidate_votes = {}
candidate_results = ""
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file
with open(file_to_load) as election_data:
    # read in the file
    file_reader = csv.reader(election_data)
    # get the header row from the csv
    headers= next(file_reader)

    for row in file_reader:
        # Add the vote to the total
        total_votes += 1
        # Check to see if the candidate's name (which is store in row[2]) is already in the list, and if not, add it to candidate_options
        # and begin tracking votes for that candidate
        if (row[2] not in candidate_options):
            candidate_options.append(row[2])
            candidate_votes[row[2]] = 0
        # Add vote to candidate's total
        candidate_votes[row[2]] += 1
    
    

# Save the results to a text file
with open(file_to_save, "w") as txt_file:

    # Print results to text file and terminal
    election_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        # retrieve vote count for each candidate
        votes = candidate_votes[candidate_name]
        # calculate the vote percentage
        vote_percentage = float("{:.1f}".format(float(votes) / float(total_votes) * 100))
        
        candidate_results = candidate_results + (f"{candidate_name}: {vote_percentage}% ({votes:,})\n")
        
        # Determine winning vote count and percentage and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    # Print candidates' results to file and terminal
    print(candidate_results)
    txt_file.write(candidate_results)

    # Print winner to file and terminal
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the vote winner and breakout to text file
    txt_file.write(winning_candidate_summary)
    

    

    


