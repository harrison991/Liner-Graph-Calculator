import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

def calculate_and_plot():
    try:
        m = float(entry_m.get())
        x_start = float(entry_x.get())
        c = float(entry_c.get())
        
        if not (-2 <= x_start <= 2):
            messagebox.showerror("Input Error", "X coordinate must be between -2 and 2.")
            return
        
        x_values = np.arange(-2, 3)  # x values from -2 to 2
        y_values = m * x_values + c  # Calculate corresponding y values

        # Clear the table
        for row in table.get_children():
            table.delete(row)
        
        # Display the table
        for x_val, y_val in zip(x_values, y_values):
            table.insert("", "end", values=(x_val, y_val))
        
        # Plot the graph
        plt.figure(figsize=(6, 6))
        plt.plot(x_values, y_values, marker='o', linestyle='-', color='b')
        plt.xlim(min(x_values)-1, max(y_values)+1)
        plt.ylim(min(y_values)-1, max(x_values)+1)
        plt.grid(True)
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)
        plt.title(f"Graph of y = {m}x + {c}")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers for the gradient, x coordinate, and y intercept.")

# Create the main window
root = tk.Tk()
root.title("Linear Graph Calculator")

# Create and place the input fields
tk.Label(root, text="Gradient (m):").grid(row=0, column=0, padx='5', pady='5')
entry_m = tk.Entry(root)
entry_m.grid(row=0, column=1, padx='5', pady='5')

tk.Label(root, text="X coordinate (start at -2):").grid(row=1, column=0, padx='5', pady='5')
entry_x = tk.Entry(root)
entry_x.grid(row=1, column=1, padx='5', pady='5')

tk.Label(root, text="Y intercept (c):").grid(row=2, column=0, padx='5', pady='5')
entry_c = tk.Entry(root)
entry_c.grid(row=2, column=1, padx='5', pady='5')

# Create a button to calculate and plot
calculate_button = tk.Button(root, text="Calculate and Plot", command=calculate_and_plot)
calculate_button.grid(row=3, columnspan=2, pady='10')

# Create a table to display x and y values
table = ttk.Treeview(root, columns=("x", "y"), show="headings", height=5)
table.heading("x", text="X")
table.heading("y", text="Y")
table.grid(row=4, columnspan=2, pady=10)

# Run the main loop
root.mainloop()