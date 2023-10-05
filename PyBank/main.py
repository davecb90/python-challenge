'''
    Goal:
        Calculate the following
        - total number of months included in the dataset
        - the net total amount of "Profit/Losses" over the entire period, then
            the average of those changes
        - the greatest increase in profits (date and amount) over the entire period
        - the greatest decrease in profits (date and amount) over the entire period

'''
import csv

import os

budget_csv = os.path.join("Resources", "budget_data.csv")

output_txt = os.path.join("Analysis", "budgetAnalysis.txt")

# set variables
monthsTotal = 0 
profitTotal = 0
previousProfit = 0
profitChange = []
biggestIncrease = ['',0]
biggestDecrease = ['',999999999]


with open(budget_csv) as budget:    
    # pnl = budget.read()
    csvReader = csv.reader(budget, delimiter=",") # make csv reader

    next(csvReader) # skip header row

    next(csvReader) # get first row of data


    monthsTotal = monthsTotal + 1
    profitChange.append(budget_csv[1])
    profitTotal = profitChange

    
    for row in csvReader:
        # month counter += operator adds 1 to the monthsTotal variable (concatenation)
        monthsTotal += 1 

        # as the loop runs, add the values in the 
        # profit/loss column to make a running total
        profitTotal += int(row[1]) 

        # subtract previous profit/loss value 
        # from current row in profit/loss column to find the change 
        newprofitChange = int(row[1]) - previousProfit 
        
        # add the change in profit for a row to a list
        profitChange.append(newprofitChange)

        # as the loop runs, set the value of previousProfit to the new row value
        # in the profit/loss column
        previousProfit = int(row[1])

        
   # for row in profitChange:
        if profitChange > biggestIncrease[1]:
            biggestIncrease[1] = profitChange
            biggestIncrease[0] = row[0]

        if profitChange < biggestDecrease[1]:
            biggestDecrease[1] = profitChange
            biggestDecrease[0] = row[0]
            

# calculate average change by dividing the sum of the profit change list by
# the amount of rows or values in the profit change list
avgChange = sum(profitChange[1]) / len(profitChange[1])

#if profitChange > biggestIncrease:
    #profitChange = biggestIncrease

#if profitChange < biggestDecrease:
   # profitChange = biggestDecrease


print("Financial Analyisis")
print("-----------------------------------")
print(f"Total Months: {monthsTotal}")
print(f"Total: ${profitTotal}")
print(f"Average Change: {avgChange}")
print(f"Greatest Increase in Profits: {biggestIncrease[0]} (${biggestIncrease[1]})")
print(f"Greatest Decrease in Profits: {biggestDecrease[0]} (${biggestDecrease[1]})")

    
    
