#Import Dependencies
import os
import csv

#Add Path of file
csvpath = os.path.join('Resources', 'election_data.csv')
#create variables 
candidates_lists = []
votes = []
percentage_votes = []
#open file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    #Loop through file to look for candidates list
    for row in csvreader:
        if row[2] not in candidates_lists:
            candidates_lists.append(row[2])
            candidates_index = candidates_lists.index(row[2])
            votes.append(1)
            
        else:
            candidates_index = candidates_lists.index(row[2])
           
            votes[candidates_index] += 1
         #sum total_vote   
    total_vote = sum(votes)
            #Create a loop to calculate percentage
    for n in range(len(candidates_lists)):
        percent = (votes[n]/total_vote) * 100
        percent_2 = (f" {str(round(percent, 3))}%")
        percentage_votes.append(percent_2)
                # create variables to find election winners
    win = max(votes)
    win_index = votes.index(win)
    win_candidate = candidates_lists[win_index]
                
                
        
        
    
            
            
            
            #Output to .txt file
output_path = "election_results.txt"
file = open(output_path, 'w')
file.write("Electoral Results\n")
file.write("--------------------------------\n")
file.write(f"Total Votes: {sum(votes)}\n")
file.write("-------------------------------------\n")
for i in range(len(candidates_lists)):
    file.write((f"{candidates_lists[i]}: {str(percentage_votes[i])} ({str(votes[i])})\n"))

file.write("----------------------------------------=\n")

file.write(f"Winner: {win_candidate}\n")
file.write("-------------------------------------------------------------\n")
            
file.close()
            