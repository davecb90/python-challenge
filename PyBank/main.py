'''
    Goal:
        Calculate the following
        - total number of months included in the dataset
        - the net total amount of "Profit/Losses" over the entire period, then
            the average of those changes
        - the greatest increase in profits (date and amount) over the entire period
        - the greatest decrease in profits (date and amount) over the entire period

'''
# import modules to read csv
import csv
import os

# path for csv file
budget_csv = os.path.join("Resources", "budget_data.csv")

# path for output file to the Analysis folder
output_txt = os.path.join("..","Analysis", "budgetAnalysis.txt")

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

    # skip header row
    next(csvReader) 

    # get first row of data and set it to a variable
    first_row = next(csvReader) 

    # add one to the month total since we are skipping the first row of data
    monthsTotal = monthsTotal + 1 
    # set the first profit and loss from the csv file as the first previous profit
    previousProfit = int(first_row[1])
    # add the first profit and loss to the profit total
    profitTotal += int(first_row[1])

    
    for row in csvReader:
        # month counter += operator adds 1 to the monthsTotal variable
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

        
        # find the largest profit and loss increase and set it to the current row
        if newprofitChange > biggestIncrease[1]:
            biggestIncrease[0] = row[0]
            biggestIncrease[1] = newprofitChange
            
        # find the largest profit and loss decrease and set it to the current row
        if newprofitChange < biggestDecrease[1]:
            biggestDecrease[0] = row[0]
            biggestDecrease[1] = newprofitChange
            
            

# calculate average change by dividing the sum of the profit change list by
# the amount of rows or values in the profit change list
avgChange = sum(profitChange) / len(profitChange)

# print the Analysis results to the terminal
print("Financial Analysis")
print("-----------------------------------")
print(f"Total Months: {monthsTotal}")
print(f"Total: ${profitTotal}")
print(f"Average Change: {avgChange}")
print(f"Greatest Increase in Profits: {biggestIncrease[0]} (${biggestIncrease[1]})")
print(f"Greatest Decrease in Profits: {biggestDecrease[0]} (${biggestDecrease[1]})")

# write the analysis results to a text file that outputs to the Analysis folder
with open (output_txt, "w") as outputTxt:
    outputTxt.write("Financial Analysis\n")
    outputTxt.write("-----------------------------------\n")
    outputTxt.write(f"Total Months: {monthsTotal}\n")
    outputTxt.write(f"Total: ${profitTotal}\n")
    outputTxt.write(f"Average Change: {avgChange}\n")
    outputTxt.write(f"Greatest Increase in Profits: {biggestIncrease[0]} (${biggestIncrease[1]})\n")
    outputTxt.write(f"Greatest Decrease in Profits: {biggestDecrease[0]} (${biggestDecrease[1]})\n")    
    
