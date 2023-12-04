#Total number of months in the data set
#Net total amount of Profit/Losses over entire period
#Changes in Profit/Losses over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period

import os
import csv

# Define csv path
budget_data_csv = os.path.join("Resources", "budget_data.csv")

# Variables
dates = []
profit_loss_change = []
Total_profit_losses = 0
Total_Months = 0
Previous_profit_loss = 0

# Read the csv file
with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip header
    header = next(csvreader) 

    for row in csvreader:
        # Get date and profit/loss
        date = row[0]
        profit_loss = int(row[1])

        # determine total number of months
        Total_Months += 1

        # determine total profit/losses
        Total_profit_losses += profit_loss

        # changes in profit/losses
        if Total_Months > 1:
            change = profit_loss - Previous_profit_loss
            profit_loss_change.append(change)
            dates.append(date)

        # reset for next iteration
        Previous_profit_loss = profit_loss

# Average change
avg_change = sum(profit_loss_change) / len(profit_loss_change)

# greatest increase & decrease
greatest_increase = max(profit_loss_change)
greatest_increase_date = dates[profit_loss_change.index(greatest_increase)]
greatest_decrease = min(profit_loss_change)
greatest_decrease_date = dates[profit_loss_change.index(greatest_decrease)]

# Print results
print("Financial Analysis")
print("----------------------------")
print(f"Total_Months: {Total_Months}")
print(f"Total: ${Total_profit_losses}")
print(f"Average Change: ${round(avg_change, 2)}")
print(f"Greatest Increase In Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease In Profits: {greatest_decrease_date} (${greatest_decrease})")

# Output as txt file
output_directory = r"C:\Users\bfletchall\Desktop\Challenge_repos\python-challenge\PyBank\Analysis\Financial_Analysis_Results.txt"
with open(output_directory, "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total_Months: {Total_Months}\n")
    output_file.write(f"Total: ${Total_profit_losses}\n")
    output_file.write(f"Average Change: ${round(avg_change, 2)}\n")
    output_file.write(f"Greatest Increase In Profits: {greatest_increase_date} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease In Profits: {greatest_decrease_date} (${greatest_decrease})\n")