# Import the necessary library for data visualization
import matplotlib.pyplot as plt

# Define sample data for expense tracking
categories = ['Food', 'Rent', 'Transportation', 'Entertainment']
expenses = [300, 500, 200, 100]  # All expenses are positive

# Check for negative expenses
negative_expenses = [expense for expense in expenses if expense < 0]

if negative_expenses:
    # If negative expenses are detected, print an error message
    print("Error: Negative expenses are not allowed.")
else:
    # Create a pie chart to visualize expense distribution
    plt.pie(expenses, labels=categories, autopct='%1.1f%%')
    plt.title('Expense Tracker')
    plt.show()

    # Create data for a table to display detailed expense information
    table_data = [['Category', 'Expense']]
    for category, expense in zip(categories, expenses):
        # Format expenses as currency and add to the table
        table_data.append([category, f'${expense}'])

    # Create a figure and axis for the table
    fig, ax = plt.subplots()
    ax.axis('tight')
    ax.axis('off')

    # Display the table on the screen
    ax.table(cellText=table_data, colLabels=None, cellLoc='center', loc='center')
    plt.show()
