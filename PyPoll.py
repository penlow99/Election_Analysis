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

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers= next(file_reader)
    print(headers)
# To do: perform analysis


