#load the file
import csv
import os 

# load,open  and read with indrect path
file_to_load=os.path.join('Resources','election_results.csv')

# load,open and write with direct and indirect path
file_to_save=os.path.join('Analysis', 'election_analysis.txt')

with open(file_to_load) as election_data:
 file_reader=csv.reader(election_data)
 header= next(file_reader)
 print(header)
    


