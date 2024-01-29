# A Single File Python Expense Tracker 

## Overview

A Python program designed to help individuals or organizations efficiently manage and visualize their expenses. It allows users to input their expense categories and corresponding expense amounts, and then provides two visual representations of expenses: a pie chart displaying the distribution of expenses across categories and a table showing detailed information about each expense category.

## Input Data

The program expects input data in the form of two lists:
- `categories`: A list of expense categories (e.g., 'Food,' 'Rent,' 'Transportation').
- `expenses`: A list of corresponding expense amounts in USD (e.g., [300, 500, 200]).

## Program Features

### Visualization

The program offers the following visualizations:

1. **Pie Chart**: A pie chart visually represents the distribution of expenses across categories. Each slice of the pie chart is labeled with the corresponding expense category, and the percentage of each category's expense relative to the total expenses is displayed on the chart.

2. **Expense Table**: A table displays detailed information about each expense category. The table contains two columns: 'Category' and 'Expense.' It is populated with rows containing category names and their respective expense amounts.

### Error Handling

The program also checks for negative expenses. If any negative expenses are detected, it prints an error message: "Error: Negative expenses are not allowed."

## How to Use

1. Ensure you have Python installed on your system.

2. Clone this GitHub repository to your local machine.

3. Modify the `categories` and `expenses` lists in the `main.py` file with your own expense data.

4. Run the program using the command `python main.py`.

5. The program will display the pie chart and the expense table based on your input data.

## Example

Suppose the input data looks like this:

categories = ['Food', 'Rent', 'Transportation', 'Entertainment']
expenses = [300, 500, 200, 100]

The program will generate visualizations for these expenses, helping one to manage finances and make informed financial decisions.

![EXPENSE-TRACKER](https://github.com/poliklinikvildan/Single_File_ExpenseTracker/assets/134360221/2057387d-f8c0-4d6a-8b28-0496584b5c51)


## Dependencies

This program relies on the `matplotlib` library for data visualization. To install `matplotlib`, you can use pip by running the following command in your terminal or command prompt:


```bash
pip install matplotlib
```


