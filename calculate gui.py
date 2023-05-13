# Import Tkinter module
from tkinter import *

# Define a function to calculate x*y and display the result
def calculate():
    # Get the values of x and y from the entry widgets
    x = float(x_entry.get())
    y = float(y_entry.get())
    # Calculate the product of x and y
    product = x * y
    # Update the text of the result label
    result_label.config(text="The output is: " + str(product))

# Create a root window
root = Tk()

# Create a label for x
x_label = Label(root, text="Enter x:")
x_label.grid(row=0, column=0)

# Create an entry widget for x
x_entry = Entry(root)
x_entry.grid(row=0, column=1)

# Create a label for y
y_label = Label(root, text="Enter y:")
y_label.grid(row=1, column=0)

# Create an entry widget for y
y_entry = Entry(root)
y_entry.grid(row=1, column=1)

# Create a button to trigger the calculation
calculate_button = Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=2, column=0, columnspan=2)

# Create a label to display the result
result_label = Label(root, text="The output is:")
result_label.grid(row=3, column=0, columnspan=2)

# Start the main loop of the window
root.mainloop()