Till tech test in Python
========================

This is a solution to Makers Academy's [Till tech test](https://github.com/makersacademy/till_tech_test) (Version 1).

This solution uses a test-driven approach, with unit and feature tests implemented using [nose tests](https://nose.readthedocs.org/en/latest/).

It also shows how JSON documents can be converted into Python.

Python 2.7 is used.

##Installation

```
$ git clone git@github.com:Andrew47/till_tech_test.git
$ cd till_tech_test
```

Create a new Python environment (either using [Virtualenv](https://virtualenv.readthedocs.org/en/latest/) or [Anaconda](http://conda.pydata.org/docs/using/envs.html)).

Python packages required are listed in `requirements.txt`.

##Usage

First create a new receipt:

```
from app.receipt import Receipt
receipt = Receipt()
```

Restaurant name, address and phone number can be found as follows:

```
print receipt.shopName
print receipt.address
print receipt.phone
```

Using the sample JSON file, these respectively return: The Coffee Connection, 123 Lakeside Way and 16503600708.

Orders need to be specified in a dictionary, with the name of each item and the amount ordered:

```
order = {"Cafe Latte": 2, "Blueberry Muffin": 1, "Choc Mudcake": 1}
```

Then the tax cost can be found - here using a 8.64% tax rate:

```
print receipt.tax(order)
```

The total cost can be found:

```
print receipt.total_cost(order)
```
The line totals can be found:

```
print receipt.line_total(order)
```

This will return (using the sample JSON file):
```
{'Blueberry Muffin': 4.05, 'Choc Mudcake': 6.4, 'Cafe Latte': 9.5}
```

Note that the number is the line total for that item.

To change the items available, their prices and the restaurant's details change the file `hipstercoffee.json`.

The guidance to this tech test is provided below:

##Version 1

Implement a system that contains the business logic to produce receipts similar to this, based on a `json` price list and test orders. A sample `.json` file has been provided with the list of products sold at this particular coffee shop.

Here are some sample orders you can try - whether you use this information is up to you:

> **Jane**  
> 2 x Cafe Latte  
> 1 x Blueberry Muffin  
> 1 x Choc Mudcake  
>
> **John**  
> 4 x Americano  
> 2 x Tiramisu  
> 5 x Blueberry Muffin  

Your receipt must calculate and show the correct amount of tax (in this shop's case, 8.64%), as well as correct line totals and total amount. Do not worry about calculating discounts or change yet. Consider what output formats may be suitable.

##Author
* [Andrew Burnie](https://github.com/Andrew47)
