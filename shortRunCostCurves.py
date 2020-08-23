import matplotlib.pyplot as plot

def createVariableCosts(quantity):
	array = []
	for i in range(0, quantity):
		array.append(float(input("Enter the variable cost when " + str(i+1) + " output is produced: ")))
	return array

def createTotalCosts(fixed_cost, variable_costs, quantity):
	array = []
	for i in range(0, quantity):
		array.append(variable_costs[i] + fixed_cost)
	return array 

def printCost(array):
	size = len(array)
	for i in range(0, size):
		print(array[i])

def createAvgCost(cost_type, quantity):
	array = []
	for i in range(0, quantity):
		array.append(float(cost_type[i]/(i+1)))
	return array

def createAvgFixedCosts(fixed_cost, quantity):
	array = []
	for i in range(0, quantity):
		array.append(float(fixed_cost)/(i+1))
	return array

def createQuantities(quantity):
	array = []
	for i in range(0, quantity):
		array.append(int(i+1))
	return array

# get inputs
total_quantity = int(input("What is the total quantity of output? "))
fixed_cost = float(input("Enter the total fixed costs: "))

# computes the costs
variable_costs = createVariableCosts(total_quantity)
total_costs = createTotalCosts(fixed_cost, variable_costs, total_quantity)
avg_variable_costs = createAvgCost(variable_costs, total_quantity)
avg_total_costs = createAvgCost(total_costs, total_quantity)
avg_fixed_costs = createAvgFixedCosts(fixed_cost, total_quantity)

quantity = createQuantities(total_quantity)

# creates the graph
plot.title("Short Run Cost Curves")
plot.xlabel("Quantity")
plot.ylabel("Price")
plot.plot(quantity, avg_variable_costs, label = "Average Variable Cost")
plot.plot(quantity, avg_fixed_costs, label = "Average Fixed Cost")
plot.plot(quantity, avg_total_costs, label = "Average Total Cost")
plot.legend()
plot.show()