# import the os module, allows us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
csvpath = os.path.join('3-Python','Homework','Instructions','PyBank','Resources','budget_data.csv')

date = []
profit_losses = []
previous_pnl = 0
total_pnl = 0
initial_diff = 0
total_pnl = 0

# Reading using CSV module
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    Row_Counter=0
    for row in csvreader:
        print(row)
        Row_Counter = Row_Counter + 1
        
        print(Row_Counter)