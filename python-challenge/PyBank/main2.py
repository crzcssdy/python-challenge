import os
import csv

# Path to the budget data CSV file
file_path = 'budget_data.csv'

# Initialize variables as counters to store the total values
total_months = 0
net_total = 0
previous_profit_loss = None
changes = []
dates = []
greatest_increase = {'date': '', 'amount': float('-inf')}
greatest_decrease = {'date': '', 'amount': float('inf')}

# Read and open the CSV file
with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)

date = row[0]

profit_loss = int(row[1])
except IndexError:
    print(f"Skipping malformed row: {row}")
    continue  # Skip the malformed row

# Increment the total number of months
total_months += 1

# Add to the net total amount of "Profit/Losses"
net_total += profit_loss

# Calculate the change in "Profit/Losses"
if previous_profit_loss is not None:
    change = profit_loss - previous_profit_loss
    changes.append(change)
    dates.append(date)

# Check for greatest increase in profits
if change > greatest_increase['amount']:
    greatest_increase['amount'] = change
    greatest_increase['date'] = date

# Check for greatest decrease in profits
if change < greatest_decrease['amount']:
    greatest_decrease['amount'] = change
    greatest_decrease['date'] = date

# Update the previous profit/loss
previous_profit_loss = profit_loss

# Calculate the average change
average_change = sum(changes) / len(changes) if changes else 0

# Prepare the analysis report
report = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n"
)

# Print the analysis to the terminal
print(report)

# Export the results to a text file
with open('financial_analysis.txt', mode='w') as file:
    file.write(report)
