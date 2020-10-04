# Election_Analysis

## Project Overview
A Colorada Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
3. Determine which county cast the largest number of votes.
4. Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
5. Determine the winner of the election based on the popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.7, Visual Studio Code 1.49.2

## Summary
The analysis of the election shows that:
- There were **369,711** votes cast in the election.

### Counties
- The counties in this precinct are:
    - **Jefferson**
    - **Denver**
    - **Arapahoe**
- The county vote results were:
    - **Jefferson** county cast **10.5%** of the vote and **38,855** number of votes.
    - **Denver** county cast **82.8%** of the vote and **306,055** number of votes.
    - **Arapahoe** county cast **6.7%** of the vote and **24,801** number of votes.
- The county with the largest turnout was:
    - **Denver**, which cast **82.8%** of the vote, for a total of **306,055** votes.

### Candidates
- The candidates were:
    - **Charles Casper Stockham**
    - **Diana DeGette**
    - **Raymon Anthony Doane**
- The candidate results were:
    - **Charles Casper Stockham** received **23.0%** of the vote and **85,213** number of votes.
    - **Diana DeGette** received **73.8%** of the vote and **272,892** number of votes.
    - **Raymon Anthony Doane** received **3.1%** of the vote and **11,606** number of votes.
- The winner of the election was:
    - **Diana DeGette**, who received **73.8%** of the vote and **272,892** number of votes.

## Challenge Overview
This challenge presented us with the problem of reading in a data file in the csv format (election_results.csv), and performing an analysis of election results on that data. Once the correct analysis had been run as instructed, the formatted results were to be saved to text file (election_analysis.txt) and printed to the screen via the terminal VS Code.

## Challenge Summary
Using the results from this election, the vote totals were determined for the precinct, each county, and the individual candidates. Per these results, it can be determined that Denver county cast the most votes in this election. As can also be seen in the analysis of this election, Diana DeGette won by a handy margin. She received more than double the votes of her competetors combined total. A breakout of the results can also be found in the "election_analysis,txt" file stored in the "Analysis" folder.

## Future Use of this Script
In the future, if given the results in the same format, the Colorada Board of Elections may chose to use this code to determine not only local congressional district election, but also determine:
- Breakdowns of state-wide elections by congressional district by changing references of county to district, such as follows:

'''python
    
    for district in district_dict:
        # 6b: Retrieve the district vote count.
        district_vote_count =  district_dict[district]
        # 6c: Calculate the percent of total votes for the district.
        district_vote_percentage = float(district_vote_count)/float(total_votes) * 100
        # 6d: Print the district results to the terminal.
        district_results = (f"{district}: {district_vote_percentage:.1f}% ({district_vote_count:,})  ")
        print(district_results)
        # 6e: Save the district votes to a text file.
        txt_file.write(district_results)
        # 6f: Write a decision statement to determine the winning district and get its vote count.
        if (district_vote_count > district_largest_votes):
            district_largest = district
            district_largest_votes = district_vote_count

    # 7: Print the district with the largest turnout to the terminal.
    district_winner = (
                    f"\n-------------------------"
                    f"\nLargest District Turnout: {district_largest}\n"
                    f"-------------------------\n")
    print(district_winner)
    # 8: Save the district with the largest turnout to a text file.
    txt_file.write(district_winner)
'''

- Breakdowns of Colorado's participation in national elections, using a states instead of counties, and focusing results on Colorado:

'''python
    
    for state in state_dict:
        # 6b: Retrieve the state vote count.
        state_vote_count =  state_dict[state]
        # 6c: Calculate the percent of total votes for the state.
        state_vote_percentage = float(state_vote_count)/float(total_votes) * 100
        # 6d: Print the state results to the terminal.
        state_results = (f"{state}: {state_vote_percentage:.1f}% ({state_vote_count:,})  ")
        print(state_results)
        # 6e: Save the state votes to a text file.
        txt_file.write(state_results)
        # 6f: Write a decision statement to determine the winning state and get its vote count.
        if (state_vote_count > state_largest_votes):
            state_largest = state
            state_largest_votes = state_vote_count
        # Store the results for the state of Colorado
        if (state == "Colorado"):
            Col_results = (f"{state}: {state_vote_percentage:.1f}% ({state_vote_count:,})  ")

    # 7: Print the state with the largest turnout to the terminal.
    state_winner = (
                    f"\n-------------------------"
                    f"\nLargest state Turnout: {state_largest}\n"
                    f"-------------------------\n")
    print(state_winner)

    # Print the results for Colorado.
    print(f"\n-------------------------"
          f"\n The results for the state of Colorado:"
          f"\n{Col_results}"
          f"\n-------------------------") 
          
    # 8: Save the state with the largest turnout to a text file.
    txt_file.write(state_winner)
'''