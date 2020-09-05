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

	def testCreateAvgFixedCosts(self):
		test_fixed_cost = 43
		test_quantity = 5
		result = shortRunCostCurves.createAvgFixedCosts(test_fixed_cost, test_quantity)
		self.assertEqual(result, [43.0, 21.5, 14.333333333333334, 10.75, 8.6])

	def testComputeTotalProfit(self):
		test_avg_total_costs = [0, 143.2, 300, 400]
		test_revenue = 1023
		result = shortRunCostCurves.computeTotalProfit(test_revenue, test_avg_total_costs, 2)
		self.assertEqual(result, 723)
		result = shortRunCostCurves.computeTotalProfit(test_revenue, test_avg_total_costs, 0)
		self.assertEqual(result, 1023)
		result = shortRunCostCurves.computeTotalProfit(test_revenue, test_avg_total_costs, 1)
		self.assertEqual(result, 879.8)

if __name__ == '__main__':
	unittest.main()