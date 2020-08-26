import matplotlib.pyplot as plot
import sys

def createVariableCosts(quantity):
	array = []
	array.append(float(0))
	for i in range(quantity):
		array.append(float(input("Enter the variable cost when " + str(i+1) + " output is produced: ")))
	return array

def createTotalCosts(fixed_cost, variable_costs, quantity):
	array = []
	for i in range(quantity):
		array.append(variable_costs[i] + fixed_cost)
	return array 

def createAvgCost(cost_type, quantity):
	array = []
	for i in range(quantity):
		array.append(float(cost_type[i]/(i+1)))
	return array

def createAvgFixedCosts(fixed_cost, quantity):
	array = []
	for i in range(quantity):
		array.append(float(fixed_cost)/(i+1))
	return array

def createQuantities(quantity):
	array = []
	for i in range(quantity):
		array.append(int(i))
	return array

def createMarginalCosts(total_costs, quantity):
	array = []
	array.append(float(0))
	for i in range(quantity-1):
		array.append(float(total_costs[i+1] - total_costs[i]))
	return array

def createMarginalRevenue(cost_per_unit, quantity):
	array = []
	for i in range(quantity):
		array.append(float(cost_per_unit))
	return array

def computeProfitMaxQuantity(marginal_revenue, marginal_costs, total_quantity):
	for i in range(total_quantity-1, -1, -1):
		if marginal_costs[i] < marginal_revenue[i]:
			return i
	return 0

def printCosts(array):
	size = len(array)
	for i in range(size):
		print(array[i])
	print()

# opening menu
user_input = 4
while True:
	try:
		user_input = int(input("How are you providing the input?\nEnter 1 for manual input\nEnter 2 to provide input from a file\nEnter 3 to exit: "))
	except:
		user_input = 4
	if user_input == 1:
		# get inputs from standard input
		total_quantity = int(input("What is the total quantity of output? "))
		cost_per_unit = float(input("Enter the cost per unit: "))
		fixed_cost = float(input("Enter the total fixed costs: "))
		variable_costs = createVariableCosts(total_quantity)
		break
	elif user_input == 2:
		#get inputs from file
	elif user_input == 3:
		sys.exit()
	else:
		print("Invalid choice, please try again")

# computes the costs
total_quantity = total_quantity + 1;
total_costs = createTotalCosts(fixed_cost, variable_costs, total_quantity)
marginal_costs = createMarginalCosts(total_costs, total_quantity)
marginal_revenue = createMarginalRevenue(cost_per_unit, total_quantity)
avg_variable_costs = createAvgCost(variable_costs, total_quantity)
avg_total_costs = createAvgCost(total_costs, total_quantity)
avg_fixed_costs = createAvgFixedCosts(fixed_cost, total_quantity)

# economical analysis
print()
print("Economical analysis:")
max_profit_quantity = computeProfitMaxQuantity(marginal_revenue, marginal_costs, total_quantity)
print("Profit maximizing quantity: " + str(max_profit_quantity))

# creates the x axis for the graph
quantity = createQuantities(total_quantity)

# creates the graph
plot.title("Short Run Cost Curves")
plot.xlabel("Quantity")
plot.ylabel("Price")

plot.plot(quantity, avg_variable_costs, label = "Average Variable Cost")
plot.plot(quantity, avg_fixed_costs, label = "Average Fixed Cost")
plot.plot(quantity, avg_total_costs, label = "Average Total Cost")
plot.plot(quantity, marginal_costs, label = "Marginal Cost")
plot.plot(quantity, marginal_revenue, label = "Marginal Revenue")
plot.legend()
plot.show()