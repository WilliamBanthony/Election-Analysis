# Add our dependencies.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
             # Print each row in the CSV file.
                #for row in file_reader:
                #     print(row)
    # Print the header row.
    headers = next(file_reader)
    print(headers)