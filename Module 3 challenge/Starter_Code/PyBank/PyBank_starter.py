# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data

change_pr_ls = 0
pr_ls_row_minus1 = 0    
greatest_increase = 0
greatest_decrease = 0

overall_changes = []
overall_changes_months = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list

    # Track the total and net change


    # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1


        # Track the net change
        total_net += int(row[1]) 

        if total_months > 1 :   
            change_pr_ls = int(row[1]) - pr_ls_row_minus1 
            overall_changes.append(change_pr_ls)
            overall_changes_months.append(row[0])   

        pr_ls_row_minus1 = int(row[1])    



        # Calculate the greatest increase in profits (month and amount)
greatest_increase = max(overall_changes)
greatest_increase_months = overall_changes_months[overall_changes.index(greatest_increase)]


        # Calculate the greatest decrease in losses (month and amount)

greatest_decrease = min(overall_changes)
greatest_decrease_months = overall_changes_months[overall_changes.index(greatest_decrease)]


# Calculate the average net change across the months

net_change_avg = sum(overall_changes) / len(overall_changes)



# Generate the output summary





# Print the output

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_net}")
print(f"Average Change: ${net_change_avg}")
print(f"Greatest Increase in Profits: {greatest_increase_months} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_months} (${greatest_decrease})")

with open(file_to_output, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("----------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${total_net}\n")
    txt_file.write(f"Average Change: ${net_change_avg:.2f}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase_months} (${greatest_increase})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease_months} (${greatest_decrease})\n")


#Write the results to a text file
#with open(file_to_output, "w") as txt_file:
#    txt_file.write(file_to_output)
#
#txt_file.write("Financial Analysis")
#txt_file.write("----------------------------")
#txt_file.write(f"Total Months: {total_months}")
#txt_file.write(f"Total: ${total_net}")
#txt_file.write(f"Average Change: ${net_change_avg}")
#txt_file.write(f"Greatest Increase in Profits: {greatest_increase_months} (${greatest_increase})")
#txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease_months} (${greatest_decrease})")
