import csv

input_file = "budget_data.csv"
output_file = "analysis.txt"

#create variables for calculations and code

total_months = 0
previous_revenue = 0
total_revenue = 0
month_of_change = []
revenue_list = []
greatest_increase = ["",0]
greatest_decrease = ["",9999999]

#create a FOR loop

with open(input_file) as revenue_data:
    reader = csv.DictReader(revenue_data)

    for row in reader:

        #The total number of months included in the dataset

        total_months = total_months + 1

        #The net total amount of "Profit/Losses" over the entire period

        total_revenue = total_revenue + int(row["Profit/Losses"])

        
        revenue_change = int(row["Profit/Losses"]) - previous_revenue
        previous_revenue = int(row["Profit/Losses"])
        revenue_list = revenue_list + [revenue_change]
        month_of_change = month_of_change + [row["Date"]]
        #The greatest increase in profits (date and amount) over the entire period
        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change
        #The greatest decrease in losses (date and amount) over the entire period
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change 

#The average of the changes in "Profit/Losses" over the entire period
average_revenue = sum(revenue_list)/len(revenue_list)

#write the code for the output
output = (
f"\nFinancial Analysis\n"
f"---------------------------------\n"
f"Total Months:{total_months}\n"
f"Total Revenue:{total_revenue}\n"
f"Average Revenue Change:{average_revenue}\n"
f"Greatest Revenue Increase: {greatest_increase[0]} (${greatest_increase[1]})\n"
f"Greatest Revenue Decrease: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
f"---------------------------------\n"
)
        
print(output)

with open(output_file,"w") as text_file:
    text_file.write(output)

