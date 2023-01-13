#load the file
import csv
import os 

# load,open  and read with indrect path
file_to_load=os.path.join('Resources','election_results.csv')

# load,open and write with direct and indirect path
file_to_save=os.path.join('Analysis', 'election_analysis.txt')
total_votes=0
Candidate_options=[]
candidate_votes={}
winning_votes=0
winning_percentage=0
winning_candidate=''
with open(file_to_load) as election_data:
 file_reader=csv.reader(election_data)
 header= next(file_reader)
 
 for row in file_reader:
    total_votes= total_votes + 1

    candidate_name=row[2]
    if candidate_name not in Candidate_options:
        Candidate_options.append(candidate_name)
        candidate_votes[candidate_name]=0
    candidate_votes[candidate_name] +=1
 for candidate_name in candidate_votes:
     votes=candidate_votes[candidate_name]
     vote_percentage = float(votes) / float(total_votes) * 100
     print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
     if (votes > winning_votes) and ( vote_percentage> winning_percentage ):
        winning_votes=votes
        winning_percentage=vote_percentage
        winning_candidate=candidate_name
     winning_candidate_summary = (
          f"-------------------------\n"
          f"Winner: {winning_candidate}\n"
          f"Winning Vote Count: {winning_votes:,}\n"
          f"Winning Percentage: {winning_percentage:.1f}%\n"
          f"-------------------------\n")
print(winning_candidate_summary)


  


   