import matplotlib.pyplot as plot
import sys

def readTotalQuantity():
	while True:
		try: 
			totalQuantity = int(input("What is the total quantity of output? "))
			if totalQuantity <= 0:
				raise ValueError()
			break
		except ValueError:
			print("Invalid quantity, please try again")
	return totalQuantity

def readPricePerUnit():
	while True:
		try: 
			pricePerUnit = float(input("Enter the price per unit: "))
			if pricePerUnit <= 0:
				raise ValueError()
			break
		except ValueError:
			print("Invalid price per unit, please try again")
	return pricePerUnit

def readFixedCost():
	while True:
		try:
			fixedCost = float(input("Enter the total fixed costs: "))
			if fixedCost <= 0:
				raise ValueError()
			break
		except ValueError:
			print("Invalid fixed cost, please try again")
	return fixedCost

# reads the variable costs from standard input and stores them into a list
def createVariableCosts(quantity):
	tempList = []
	tempList.append(float(0))
	for i in range(1, quantity+1):
		while True:
			try:
				tempItem = float(input("Enter the variable cost when " + str(i) + " output is produced: "))
				if tempItem == 0:
					print("Variable cost can not be 0, please try again\n")
				elif tempItem < 0:
					print("Variable cost can not be less than 0, please try again\n")
				elif tempItem < tempList[i-1]:
					print("Variable costs can not be decreasing as output increases, please try again\n")
				else:
					tempList.append(tempItem)
					break
			except ValueError:
				print("Invalid input for variable cost, please try again\n")
	return tempList

# checks if the file is the appropriate size for reading
def checkFileSize(file):
	fileContents = file.readlines()
	file.seek(0)
	if(len(fileContents) != (int(fileContents[0]) + 3)):
		raise ValueError()

def readTotalQuantityFromFile(file):
	totalQuantity = int(file.readline())
	if totalQuantity <= 0:
		raise ValueError()

def readPricePerUnitFromFile(file):
	pricePerUnit = float(file.readline())
	if pricePerUnit <= 0:
		raise ValueError()

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

# computes the profit maximizing quantity by looking for the quantity just below or equal
# to the point where the marginal cost is equal to the marginal revenue
def computeProfitMaxQuantity(marginalRevenue, marginalCosts, totalQuantity):
	for i in range(totalQuantity-1, -1, -1):
		if marginalCosts[i] <= marginalRevenue[i]:
			return i
	return 0

# computes the total revenue with the formula profit maximizing quantity * 
# marginal revenue at the profit maximizing quantity
def computeTotalRevenue(marginalRevenue, maxProfitQuantity):
	return marginalRevenue[maxProfitQuantity] * maxProfitQuantity

# computes the total profit with the formula total revenue - 
# total cost at the profit maximizing quantity
def computeTotalProfit(totalRevenue, totalCosts, maxProfitQuantity):
	return totalRevenue - totalCosts[maxProfitQuantity]

# prints a statement in the economic analysis if the shut down rule is met
# (when the price per unit is less than the average variable cost)
def checkShutDownRule(pricePerUnit, avgVariableCosts, maxProfitQuantity):
	if(pricePerUnit < avgVariableCosts[maxProfitQuantity]):
		print("This firm should shut down")

# creates a list from 0 to the quantity
def createQuantities(quantity):
	tempList = []
	for i in range(quantity):
		tempList.append(int(i))
	return tempList

# a function to print a list for testing
def printCosts(tempList):
	size = len(tempList)
	for i in range(size):
		print(tempList[i])
	print()

if __name__ == '__main__':
	# opening menu
	while True:
		try:
			userInput = int(input("How are you providing the input?\nEnter 1 for manual input\nEnter 2 to provide input from a file\nEnter 3 to exit\n"))
		except:
			userInput = 4
		# get inputs from standard input
		if userInput == 1:
			totalQuantity = readTotalQuantity()
			pricePerUnit = readPricePerUnit()
			fixedCost = readFixedCost()
			variableCosts = createVariableCosts(totalQuantity)
			break
		# get inputs from file
		elif userInput == 2:
			while True:
				try:
					file_name = str(input("Enter the path of the file you wish to use or type \"exit\" to exit: "))
					if file_name == "exit":
						sys.exit()
					file = open(file_name, "r")
					checkFileSize(file)
					totalQuantity = readTotalQuantityFromFile()
					pricePerUnit = readPricePerUnitFromFile()
					fixedCost = float(file.readline())
					variableCosts = createVariableCostsFromFile(totalQuantity, file)
					file.close()
					break
				except FileNotFoundError:
					print("File not found. Please try again")
				except ValueError:
					print("Invalid input found in file, please try again")
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
	maxProfitQuantity = computeProfitMaxQuantity(marginalRevenue, marginalCosts, totalQuantity)
	totalRevenue = computeTotalRevenue(marginalRevenue, maxProfitQuantity)
	totalProfit = computeTotalProfit(totalRevenue, totalCosts, maxProfitQuantity)
	print()
	print("Economical analysis:")
	print("Profit maximizing quantity: " + str(maxProfitQuantity))
	print("Total Revenue: " + str(totalRevenue))
	print("Total Profit: " + str(totalProfit))
	checkShutDownRule(pricePerUnit, avgVariableCosts, maxProfitQuantity)

	# creates the x axis for the graph
	quantity = createQuantities(totalQuantity)

	# creates the labels for the graph
	plot.title("Short-Run Cost Curves")
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