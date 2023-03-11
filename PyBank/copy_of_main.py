#Import dependencies and create variables
import os
import csv
total_months = 0
net_total = 0
net_change = 0
greatest_inc = ["", 0]
greatest_dec =["", 99999999999999999999]


profit_loss = []
months = []

net_change_list = []
#Get path to csv file
csvpath = os.path.join ('Resources', 'budget_data.csv')
# Open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    # skip header row
    next(csvreader)
    # Extract first row to avoid appending to net_change_list
    first_row = next(csvreader)
    total_months += 1
    net_total += int(first_row[1])
    prev_net = int(first_row[1])
        
        # Loop through file to get net_total and net_change
    for row in csvreader:
        total_months +=1
        net_total += int(row[1])
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
    
        net_change_list += [net_change]
        months += [row[0]]
        
        
            # use Conditionals to find greatst increase and decrease in profits
        if net_change > greatest_inc[1]:
            greatest_inc[0] = row[0]
            greatest_inc[1] = net_change

        if net_change < greatest_dec[1]:
            greatest_dec[0] = row[0]
            greatest_dec[1] = net_change

        net_monthly_avg = sum(net_change_list) / len(net_change_list)



# output to .txt file
output = (
    f"Financial Analysis\n"
    f"---------------------------------------------\n"
    f"Total Months: {total_months} \n"
    f"Total: {net_total}\n"
    f"Average Change: {net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_inc[0]} (${greatest_inc[1]})\n "
    f"Greatest Decrease in Profits: {greatest_dec[0]} (${greatest_dec[1]})\n") 

print(output)   
with open("budget_analysis.txt", "w") as txt_file:
    txt_file.write(output)
    

     
                

                
      

