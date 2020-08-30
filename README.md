# Short-Run Cost Curves
This is a small python project where I get user input to compute the short-run cost curves and run basic economic analysis for a firm in a perfectly competitve market.

## Dependencies
Tkinter
```
sudo apt-get install python3-tk
```

Matplotlib (for Python 3)
```
python3 -m pip install matplotlib
```

## Usage
If a file is being used for input, the numbers in the text file must be provided in the following order:
total quantity
price per unit
fixed cost
variable costs

notes: 
    -if the number of variable costs is greater than the total quantity, the program will only read the number of variable costs equal to the total quantity 
    -the script will not accept any value less than or equal to 0 for the total quantity and price per unit

Run the script with the following command:
```
python3 shortRunCostCurves.py
```

Run the unit tests with the following command:
```
python3 test_shortRunCostCurves.py -b
```
