# Dependencies
import os
import csv

# Load csv file
file_path = os.path.join("PyBank", "Resources", "budget_data.csv")

with open(file_path) as csvfile:
    budget_data = csv.reader(csvfile, delimiter=",")
    print(type(budget_data))
    # store the headers in a seperate variable
    headings = next(budget_data)
    
    # Set counters
    total_month = 0
    total_amount = 0
    date_list = []
    profit_list = []
    monthly_change = []

    # Find the total number of month and total profit/losses
    for row in budget_data:
        total_month += 1
        total_amount += int(row[1])
        date_list.append(row[0])
        profit_list.append(int(row[1]))
    
    # Find month-to-month change
    for x in range(len(profit_list) - 1):
        monthly_change.append(profit_list[x+1] - profit_list[x])

    # Average changes
    avg_change = sum(monthly_change)/len(monthly_change)

    #Greatest increase/decrease
    greatest_increase = max(monthly_change)
    greatest_decrease = min(monthly_change)

    #Find the date of greatest increase/decrease
    # + 1 because the date associate with the change is next month
    date_increase = date_list[monthly_change.index(greatest_increase) + 1]
    date_decrease = date_list[monthly_change.index(greatest_decrease) + 1]
    print(date_decrease)

    # print analysis statements
    print("Finalcial Analysis \n----------------------------")
    print(f"Total Month: {total_month}")
    print(f"Total: ${total_amount}")
    print(f"Average Change: ${round(avg_change,2)}")
    print(f"Greatest Increase in Profits: {date_increase} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {date_decrease} (${greatest_decrease})")

    # export the results as a text file
    output_path = os.path.join("PyBank", "analysis", "PyBank_analysis_results.txt")
    lines = ["Finalcial Analysis \n----------------------------", 
    f"Total Month: {total_month}",f"Total: ${total_amount}",
    f"Average Change: ${round(avg_change,2)}", 
    f"Greatest Increase in Profits: {date_increase} (${greatest_increase})",
    f"Greatest Decrease in Profits: {date_decrease} (${greatest_decrease})"]
    
    with open(output_path, 'w') as f:
        for l in lines:
            f.write(l)
            f.write("\n")