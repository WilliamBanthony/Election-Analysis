# Election-Analysis
## Overview of Election Audit
The purpose of this election audit was to general stats about the election including total votes cast voter turnout rate in each county, and the percentage and total amount of votes cast for each candidate as well as the winner of the election. 
## Election Audit Results
* By counting each row I was able to determine there was 369,711 votes cast.
* Jefferson county accounted for 10.5% of the votes cast which amounted to 38,855 votes.
	Denver county accounted for 82.8% of the votes cast which amounted to 306,055 votes.
	Arapahoe county accounted for 6.7% of the votes cast which amounted to 23,801 votes.
* The county that had the largest number of votes cast was Denver county.
* Charles Casper Stockham received 23% of the votes which amounted to 85,213 votes.
	Diana DeGette received 73.8% of the votes which amounted to 272,892 votes.
	Raymon Anthony Doane received 3.1% of the votes which amounted to 11,606 votes.
* Diana DeGette received the most votes and thus won the election with 73.8% of the votes which amounted to 272,892 votes.

## Election-Audit Summary
This is an excellent script that does not much modification at all to be used for any election. There are two major modifications that must be made for it to be functional though.
One modification is the loading path. Below is the code:
	# Add a variable to load a file from a path.
	file_to_load = os.path.join("Resources", "election_results.csv")

election_results.csv related to the comma-separated values that I used and Resources related to the folder the file was in. These will need to be altered to fit the new files.

Another modification is the loading path. Below is the code:
* file_to_save = os.path.join("results", "election_results.txt")

This relates to the text file that I created with the analysis. This will need to be altered if you do not want to overwrite your analysis of previous election results. 

A last modification must be made to where the code receives it's values from the csv file. Below is the code:
* candidate_name = row[2]
* county_name = row[1]

These rows numbers will have to be altered if the csv file of other elections do not place the candidate name and county name in the same location

