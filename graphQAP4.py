# A program to graph monthly sales
# written: Ryan Crowley
# date: March 24th, 2023

# imports for graphing
import matplotlib.pyplot as plt
import calendar


#inputs to get monthly sales for y-axis
sales = []
monInput = []
for i in range(1, 13):
    monInput.append(calendar.month_name[i])

for month in monInput:
    sales.append(float(input(f"Enter the total sales for {month}: ")))

#setting up list for x-axis
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


plt.title("Year to Date Sales ($)")
plt.xlabel("Months")
plt.ylabel("Total Monthly Sales ($)")
plt.plot(months, sales)
plt.show()


