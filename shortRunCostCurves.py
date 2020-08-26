import matplotlib.pyplot as plot
import sys

# reads the variable costs from standard input and stores them into a list
def createVariableCosts(quantity):
	tempList = []
	tempList.append(float(0))
	for i in range(quantity):
		tempList.append(float(input("Enter the variable cost when " + str(i+1) + " output is produced: ")))
	return tempList

# reads the variable costs from a file and stores them into a list
def createVariableCostsFromFile(quantity, file):
	tempList = []
	tempList.append(float(0))
	for i in range(quantity):
		tempList.append(float(file.readline()))
	return tempList

# creates a list for total costs with the formula total cost = variable cost + fixed cost
def createTotalCosts(fixed_cost, variable_costs, quantity):
	tempList = []
	for i in range(quantity):
		tempList.append(variable_costs[i] + fixed_cost)
	return tempList 

# creates a list for the average costs of either the total costs or variable costs with the
# formula average cost = cost at a specific quantity / the specific quantity
def createAvgCost(cost_type, quantity):
	tempList = []
	for i in range(quantity):
		tempList.append(float(cost_type[i]/(i+1)))
	return tempList

# creates a list for the average fixed costs
def createAvgFixedCosts(fixed_cost, quantity):
	tempList = []
	for i in range(quantity):
		tempList.append(float(fixed_cost)/(i+1))
	return tempList

# creates a list from 0 to the quantity
def createQuantities(quantity):
	tempList = []
	for i in range(quantity):
		tempList.append(int(i))
	return tempList

# creates a list for the marginal costs with the formula
# maginal cost = total cost at a specified quantity - total cost at the previous quantity
def createMarginalCosts(total_costs, quantity):
	tempList = []
	tempList.append(float(0))
	for i in range(quantity-1):
		tempList.append(float(total_costs[i+1] - total_costs[i]))
	return tempList

# creates a list representing the marginal revenue which is equal to the price per unit
def createMarginalRevenue(price_per_unit, quantity):
	tempList = []
	for i in range(quantity):
		tempList.append(float(price_per_unit))
	return tempList

# computes the profit maximizing quantity by looking for the quantity just below the point
# where the marginal cost is equal to the marginal revenue
def computeProfitMaxQuantity(marginal_revenue, marginal_costs, total_quantity):
	for i in range(total_quantity-1, -1, -1):
		if marginal_costs[i] < marginal_revenue[i]:
			return i
	return 0

# computes the total revenue with the formula profit maximizing quantity * 
# marginal revenue at the profit maximizing quantity
def computeTotalRevenue(marginal_revenue, max_profit_quantity):
	return marginal_revenue[max_profit_quantity] * max_profit_quantity

# computes the total profit with the formula total revenue - 
# (average total cost * average total cost at the profit maximizing quantity)
def computeTotalProfit(total_revenue, avg_total_costs, max_profit_quantity):
	return total_revenue - (avg_total_costs[max_profit_quantity] * max_profit_quantity)

# a function to print a list
def printCosts(tempList):
	size = len(tempList)
	for i in range(size):
		print(tempList[i])
	print()

# opening menu
while True:
	try:
		userInput = int(input("How are you providing the input?\nEnter 1 for manual input\nEnter 2 to provide input from a file\nEnter 3 to exit\n"))
	except:
		userInput = 4
	# get inputs from standard input
	if userInput == 1:
		total_quantity = int(input("What is the total quantity of output? "))
		price_per_unit = float(input("Enter the price per unit: "))
		fixed_cost = float(input("Enter the total fixed costs: "))
		variable_costs = createVariableCosts(total_quantity)
		break
	# get inputs from file
	elif userInput == 2:
		file_name = str(input("Enter the name of the file you wish to be use: "))
		file = open(file_name, "r")
		total_quantity = int(file.readline())
		price_per_unit = float(file.readline())
		fixed_cost = float(file.readline())
		variable_costs = createVariableCostsFromFile(total_quantity, file)
		file.close()
		break
	# exits the program
	elif userInput == 3:
		sys.exit()
	else:
		print("Invalid choice, please try again")

# computes the costs
total_quantity = total_quantity + 1;
total_costs = createTotalCosts(fixed_cost, variable_costs, total_quantity)
marginal_costs = createMarginalCosts(total_costs, total_quantity)
marginal_revenue = createMarginalRevenue(price_per_unit, total_quantity)
avg_variable_costs = createAvgCost(variable_costs, total_quantity)
avg_total_costs = createAvgCost(total_costs, total_quantity)
avg_fixed_costs = createAvgFixedCosts(fixed_cost, total_quantity)

# economical analysis
print()
print("Economical analysis:")
max_profit_quantity = computeProfitMaxQuantity(marginal_revenue, marginal_costs, total_quantity)
total_revenue = computeTotalRevenue(marginal_revenue, max_profit_quantity)
total_profit = computeTotalProfit(total_revenue, avg_total_costs, max_profit_quantity)
print("Profit maximizing quantity: " + str(max_profit_quantity))
print("Total Revenue: " + str(total_revenue))
print("Total Profit: " + str(total_profit))

# creates the x axis for the graph
quantity = createQuantities(total_quantity)

# creates the labels for the graph
plot.title("Short Run Cost Curves")
plot.xlabel("Quantity")
plot.ylabel("Price")

# plots the graph
plot.plot(quantity, avg_variable_costs, label = "Average Variable Cost")
plot.plot(quantity, avg_fixed_costs, label = "Average Fixed Cost")
plot.plot(quantity, avg_total_costs, label = "Average Total Cost")
plot.plot(quantity, marginal_costs, label = "Marginal Cost")
plot.plot(quantity, marginal_revenue, label = "Marginal Revenue")
plot.legend()
plot.show()