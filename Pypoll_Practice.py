#load the file
import csv
import os 

# load,open and read with direct path
file_to_load= 'Resources/election_results.csv'
#open the file to read
with open(file_to_load) as election_data:
    print(election_data)#

# load,open  and read with indrect path
file_to_load=os.path.join('Resources','election_results.csv')
with open(file_to_load) as election_data:
#read with reader
  file_reader=csv.reader(election_data)
for a in file_reader:
    print(a)
# load,open and write with direct and indirect path
file_to_save=os.path.join('Analysis', 'election_analysis.txt')
with open(file_to_save,'w') as txt_file:
    txt_file.write("Counties in the election\n--\nAraphobe\nDenver\njefferson")


    


