import tkinter as tk

def calculate_direct_method():
    # Retrieve user inputs
    principal = float(initial_deposit_entry.get())
    years = int(years_to_compound_entry.get())
    annual_rate = float(annual_return_rate_entry.get()) / 100

    # Direct method formula
    result = principal * (1 + annual_rate) ** years

    # Display the result
    result_label.config(text=f"Result: ${result:,.2f}")

def clear_fields():
    # Clear all entries and labels /Users/samchan/Project01/GPT.py
    initial_deposit_entry.delete(0, tk.END)
    years_to_compound_entry.delete(0, tk.END)
    annual_return_rate_entry.delete(0, tk.END)
    result_label.config(text="")

def quit_app():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Interest Calculation Tool")

# Set a larger window size, approximately 1.5x the default
root.geometry("450x300")

# Create and grid the widgets, all centered
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

tk.Label(frame, text="Initial Deposit:").grid(row=0, column=0)
initial_deposit_entry = tk.Entry(frame)
initial_deposit_entry.grid(row=0, column=1)

tk.Label(frame, text="Years to Compound:").grid(row=1, column=0)
years_to_compound_entry = tk.Entry(frame)
years_to_compound_entry.grid(row=1, column=1)

tk.Label(frame, text="Annual Return Rate (%):").grid(row=2, column=0)
annual_return_rate_entry = tk.Entry(frame)
annual_return_rate_entry.grid(row=2, column=1)

calculate_button = tk.Button(frame, text="Calculate Result", command=calculate_direct_method)
calculate_button.grid(row=3, column=0, columnspan=2)

clear_button = tk.Button(frame, text="Clear", command=clear_fields)
clear_button.grid(row=4, column=0, columnspan=2)

quit_button = tk.Button(frame, text="Quit", command=quit_app)
quit_button.grid(row=5, column=0, columnspan=2)

result_label = tk.Label(frame, text="")
result_label.grid(row=6, column=0, columnspan=2)

# Start the main event loop
root.mainloop()
