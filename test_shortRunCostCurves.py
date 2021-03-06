import unittest
from unittest import mock
from unittest import TestCase
import shortRunCostCurves

class TestShortRunCostCurves(unittest.TestCase):
	@mock.patch('shortRunCostCurves.input', create=True)
	def testReadTotalQuantity(self, mocked_input):
		mocked_input.side_effect = [0, -3, -12, "test", "useless string", " test2", 7]
		result = shortRunCostCurves.readTotalQuantity()
		self.assertEqual(result, 7)

	@mock.patch('shortRunCostCurves.input', create=True)
	def testReadPricePerUnit(self, mocked_input):
		mocked_input.side_effect = [-40, -33.0, "test", "useless string", " test2", 0, 0.0, 12]
		result = shortRunCostCurves.readPricePerUnit()
		self.assertEqual(result, 12.0)

	@mock.patch('shortRunCostCurves.input', create=True)
	def testReadFixedCost(self, mocked_input):
		mocked_input.side_effect = [0.0, -50, "test", "useless string", " test2", 30]
		result = shortRunCostCurves.readFixedCost()
		self.assertEqual(result, 30.0)

	@mock.patch('shortRunCostCurves.input', create=True)
	def testCreateVariableCosts(self, mocked_input):
		mocked_input.side_effect = [10, "useless string", 30, "test", 50, " test2", 70]
		result = shortRunCostCurves.createVariableCosts(4)
		self.assertEqual(result, [0.0, 10.0, 30.0, 50.0, 70.0])

	def testCreateTotalCosts(self):
		test_quantity = 5
		test_variable_costs = [70, 90, 130, 170, 190]
		test_fixed_cost = 40
		test_fixed_cost2 = 11
		result = shortRunCostCurves.createTotalCosts(test_fixed_cost, test_variable_costs, test_quantity)
		self.assertEqual(result, [110.0, 130.0, 170.0, 210.0, 230.0])
		result = shortRunCostCurves.createTotalCosts(test_fixed_cost2, test_variable_costs, test_quantity)
		self.assertEqual(result, [81.0, 101.0, 141.0, 181.0, 201.0])

	def testCreateAvgCost(self):
		test_quantity = 6
		test_costs = [3, 4, 9, 16, 25, 36]
		expected = [3, 2, 3, 4, 5, 6]
		result = shortRunCostCurves.createAvgCost(test_costs, test_quantity)
		self.assertEqual(result, expected)

	def testCreateMarginalRevenue(self):
		test_prices = [30, 90, 96, 1000, 2000]
		result = shortRunCostCurves.createMarginalRevenue(30, 7)
		self.assertEqual(result, [0, 30, 30, 30, 30, 30, 30])
		result = shortRunCostCurves.createMarginalRevenue(1000, 2)
		self.assertEqual(result, [0, 1000])
		result = shortRunCostCurves.createMarginalRevenue(6, 11)
		self.assertEqual(result, [0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])

	def testCreateAvgFixedCosts(self):
		test_fixed_cost = 43
		test_quantity = 5
		result = shortRunCostCurves.createAvgFixedCosts(test_fixed_cost, test_quantity)
		self.assertEqual(result, [43.0, 21.5, 14.333333333333334, 10.75, 8.6])

	def testComputeTotalProfit(self):
		test_avg_total_costs = [0.0, 143.2, 300.0, 400.0]
		test_revenue = 1023
		result = shortRunCostCurves.computeTotalProfit(test_revenue, test_avg_total_costs, 2)
		self.assertEqual(result, 723)
		result = shortRunCostCurves.computeTotalProfit(test_revenue, test_avg_total_costs, 0)
		self.assertEqual(result, 1023)
		result = shortRunCostCurves.computeTotalProfit(test_revenue, test_avg_total_costs, 1)
		self.assertEqual(result, 879.8)
		result = shortRunCostCurves.computeTotalProfit(test_revenue, test_avg_total_costs, 3)
		self.assertEqual(result, 623)

	def testComputeProfitMaxQuantity(self):
		test_marginal_revenue = [0, 30, 60, 90, 120, 150, 180]
		test_marginal_costs = [0, 40, 80, 120, 160, 200, 240]
		test_marginal_costs2 = [0, 20, 40, 60, 80, 100, 120]
		test_marginal_costs3 = [0, 20, 40, 60, 120, 170, 190]
		test_marginal_costs4 = [0, 10, 30, 50, 70, 140, 190]
		test_quantity = 7
		result = shortRunCostCurves.computeProfitMaxQuantity(test_marginal_revenue, test_marginal_costs, test_quantity)
		self.assertEqual(result, 0)
		result = shortRunCostCurves.computeProfitMaxQuantity(test_marginal_revenue, test_marginal_costs2, test_quantity)
		self.assertEqual(result, 6)
		result = shortRunCostCurves.computeProfitMaxQuantity(test_marginal_revenue, test_marginal_costs3, test_quantity)
		self.assertEqual(result, 4)
		result = shortRunCostCurves.computeProfitMaxQuantity(test_marginal_revenue, test_marginal_costs4, test_quantity)
		self.assertEqual(result, 5)

	def testComputeTotalRevenue(self):
		test_marginal_revenue = [0, 40, 60, 80, 100, 120, 140]
		result = shortRunCostCurves.computeTotalRevenue(test_marginal_revenue, 3)
		self.assertEqual(result, 240)
		result = shortRunCostCurves.computeTotalRevenue(test_marginal_revenue, 0)
		self.assertEqual(result, 0)
		result = shortRunCostCurves.computeTotalRevenue(test_marginal_revenue, 5)
		self.assertEqual(result, 600)

	def testComputeTotalProfit(self):
		test_total_revenue = 1000
		test_total_costs = [0, 100, 200, 300, 400, 1200]
		result = shortRunCostCurves.computeTotalProfit(test_total_revenue, test_total_costs, 0)
		self.assertEqual(result, 1000)
		result = shortRunCostCurves.computeTotalProfit(test_total_revenue, test_total_costs, 3)
		self.assertEqual(result, 700.0)
		result = shortRunCostCurves.computeTotalProfit(test_total_revenue, test_total_costs, 5)
		self.assertEqual(result, -200.0)

	def testCreateQuantities(self):
		expected1 = [0, 1, 2, 3, 4, 5]
		expected2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
		result1= shortRunCostCurves.createQuantities(6)
		result2 = shortRunCostCurves.createQuantities(12)
		self.assertEqual(expected1, result1)
		self.assertEqual(expected2, result2)


if __name__ == '__main__':
	unittest.main()
