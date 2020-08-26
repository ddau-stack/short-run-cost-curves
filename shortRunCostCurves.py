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
def createTotalCosts(fixedCost, variableCosts, quantity):
	tempList = []
	for i in range(quantity):
		tempList.append(variableCosts[i] + fixedCost)
	return tempList 

# creates a list for the average costs of either the total costs or variable costs with the
# formula average cost = cost at a specific quantity / the specific quantity
def createAvgCost(cost_type, quantity):
	tempList = []
	for i in range(quantity):
		tempList.append(float(cost_type[i]/(i+1)))
	return tempList

# creates a list for the average fixed costs
def createAvgFixedCosts(fixedCost, quantity):
	tempList = []
	for i in range(quantity):
		tempList.append(float(fixedCost)/(i+1))
	return tempList

# creates a list from 0 to the quantity
def createQuantities(quantity):
	tempList = []
	for i in range(quantity):
		tempList.append(int(i))
	return tempList

# creates a list for the marginal costs with the formula
# maginal cost = total cost at a specified quantity - total cost at the previous quantity
def createMarginalCosts(totalCosts, quantity):
	tempList = []
	tempList.append(float(0))
	for i in range(quantity-1):
		tempList.append(float(totalCosts[i+1] - totalCosts[i]))
	return tempList

# creates a list representing the marginal revenue which is equal to the price per unit
def createMarginalRevenue(pricePerUnit, quantity):
	tempList = []
	for i in range(quantity):
		tempList.append(float(pricePerUnit))
	return tempList

# computes the profit maximizing quantity by looking for the quantity just below the point
# where the marginal cost is equal to the marginal revenue
def computeProfitMaxQuantity(marginalRevenue, marginalCosts, totalQuantity):
	for i in range(totalQuantity-1, -1, -1):
		if marginalCosts[i] < marginalRevenue[i]:
			return i
	return 0

# computes the total revenue with the formula profit maximizing quantity * 
# marginal revenue at the profit maximizing quantity
def computeTotalRevenue(marginalRevenue, maxProfitQuantity):
	return marginalRevenue[maxProfitQuantity] * maxProfitQuantity

# computes the total profit with the formula total revenue - 
# (average total cost * average total cost at the profit maximizing quantity)
def computeTotalProfit(totalRevenue, avgTotalCosts, maxProfitQuantity):
	return totalRevenue - (avgTotalCosts[maxProfitQuantity] * maxProfitQuantity)

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
		totalQuantity = int(input("What is the total quantity of output? "))
		pricePerUnit = float(input("Enter the price per unit: "))
		fixedCost = float(input("Enter the total fixed costs: "))
		variableCosts = createVariableCosts(totalQuantity)
		break
	# get inputs from file
	elif userInput == 2:
		file_name = str(input("Enter the name of the file you wish to be use: "))
		file = open(file_name, "r")
		totalQuantity = int(file.readline())
		pricePerUnit = float(file.readline())
		fixedCost = float(file.readline())
		variableCosts = createVariableCostsFromFile(totalQuantity, file)
		file.close()
		break
	# exits the program
	elif userInput == 3:
		sys.exit()
	else:
		print("Invalid choice, please try again")

# computes the costs
totalQuantity = totalQuantity + 1;
totalCosts = createTotalCosts(fixedCost, variableCosts, totalQuantity)
marginalCosts = createMarginalCosts(totalCosts, totalQuantity)
marginalRevenue = createMarginalRevenue(pricePerUnit, totalQuantity)
avgVariableCosts = createAvgCost(variableCosts, totalQuantity)
avgTotalCosts = createAvgCost(totalCosts, totalQuantity)
avgFixedCosts = createAvgFixedCosts(fixedCost, totalQuantity)

# economical analysis
print()
print("Economical analysis:")
maxProfitQuantity = computeProfitMaxQuantity(marginalRevenue, marginalCosts, totalQuantity)
totalRevenue = computeTotalRevenue(marginalRevenue, maxProfitQuantity)
totalProfit = computeTotalProfit(totalRevenue, avgTotalCosts, maxProfitQuantity)
print("Profit maximizing quantity: " + str(maxProfitQuantity))
print("Total Revenue: " + str(totalRevenue))
print("Total Profit: " + str(totalProfit))

# creates the x axis for the graph
quantity = createQuantities(totalQuantity)

# creates the labels for the graph
plot.title("Short Run Cost Curves")
plot.xlabel("Quantity")
plot.ylabel("Price")

# plots the graph
plot.plot(quantity, avgVariableCosts, label = "Average Variable Cost")
plot.plot(quantity, avgFixedCosts, label = "Average Fixed Cost")
plot.plot(quantity, avgTotalCosts, label = "Average Total Cost")
plot.plot(quantity, marginalCosts, label = "Marginal Cost")
plot.plot(quantity, marginalRevenue, label = "Marginal Revenue")
plot.legend()
plot.show()