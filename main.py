#First we will import the os module
#This will allow us to create file paths across operating systems
import os

#Module for reading CSV files
import csv

# Declare file location through pathlib
path = "/Users/basantagurung/Desktop/Python-Challenge/Resources"
csvpath = os.path.join(path, "budget_data.csv")

#set the output of the text file
text_path = "output.txt"


# Set variables
total_months = 0
total_revenue = 0
revenue = []
previous_revenue = 0
monthly_change = []
revenure_change = 0
greatest_decrease = ["", 9999999]
greatest_increase = ["", 0]
revenue_change_list = []
revenue_average = 0

 
# Open csv in default read mode with context manager
with open(csvpath, newline = '') as csvfile:
    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)
    
    print(csvreader)
    
    #Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: n{csv_header}")
    
    #Read each row of data after the header
    for row in csvreader:
        print(row)
        
       