import tkinter as tk
from tkinter import messagebox

def show_message_and_close(message):
    messagebox.showinfo("Message", message)
    window.destroy()

def show_fruit_selection():
    fruit_window = tk.Toplevel(window)
    fruit_window.title("THESE ARE THE AVAILABLE PRODUCTS IN OUR SHOP")
    fruit_window.geometry("500x500")
    fruit_window.configure(bg="#B3E0FF")  # Light Blue

    tk.Label(fruit_window, text="Choose the fruits you want to buy:", font=("Comic Sans MS", 16), bg="#B3E0FF").pack(pady=10)

    for fruit in fruits:
        tk.Checkbutton(fruit_window, text=fruit, variable=selected_fruits[fruit], font=("Comic Sans MS", 14), bg="#B3E0FF").pack()

    tk.Button(fruit_window, text="Submit", command=show_quantity_selection, font=("Comic Sans MS", 16), bg="#4CAF50", fg="white").pack(pady=20)

def show_quantity_selection():
    quantity_window = tk.Toplevel(window)
    quantity_window.title("PLEASE INDICATE THE AMOUNT OF EACH ITEM YOU WANT TO BUY IN THIS SHOP")
    quantity_window.geometry("500x500")
    quantity_window.configure(bg="#C8E6C9")  # Light Green

    tk.Label(quantity_window, text="Enter the quantity for each selected item:", font=("Comic Sans MS", 16), bg="#C8E6C9").pack(pady=10)

    for fruit, var in selected_fruits.items():
        if var.get():
            tk.Label(quantity_window, text=f"{fruit}s:", font=("Comic Sans MS", 14), bg="#C8E6C9").pack()
            tk.Entry(quantity_window, textvariable=quantities[fruit], font=("Comic Sans MS", 14)).pack(pady=5)

    tk.Button(quantity_window, text="Submit", command=show_price_summary, font=("Comic Sans MS", 16), bg="#4CAF50", fg="white").pack(pady=20)

def show_price_summary():
    summary_window = tk.Toplevel(window)
    summary_window.title("THESE ARE THE OVERALL AMOUNT AND THE PRICES OF EACH YOU HAVE CHOSEN IN THE PREVIOUS SECTIONS")
    summary_window.geometry("600x600")
    summary_window.configure(bg="#FFCCCB")  # Light Coral

    total_amount = 0

    for fruit, var in selected_fruits.items():
        if var.get():
            price = prices[fruit] * quantities[fruit].get()
            total_amount += price
            tk.Label(summary_window, text=f"{fruit}: {quantities[fruit].get()} at {prices[fruit]} pesos each = {price} pesos",
                     font=("Comic Sans MS", 14), bg="#FFCCCB").pack(pady=5)

    tk.Label(summary_window, text=f"Overall amount: {total_amount} pesos", font=("Comic Sans MS", 16), bg="#FFCCCB").pack(pady=20)

    tk.Button(summary_window, text="Submit", command=lambda: show_message_and_close("Thank you for shopping with us! We hope to see you again. God Bless!"),
              font=("Comic Sans MS", 16), bg="#4CAF50", fg="white").pack(pady=10)
    tk.Button(summary_window, text="Cancel", command=lambda: show_message_and_close("We're very sorry for not meeting your expectations. Thank you for visiting us and Have a Great Day!"),
              font=("Comic Sans MS", 16), bg="#FF6347", fg="white").pack(pady=10)

def on_submit():
    if section.get() == "A":
        window.withdraw()
        show_fruit_selection()

window = tk.Tk()
window.title("WELCOME TO MY FRUIT SHOP, HOW MAY I HELP YOU?")
window.geometry("800x800")
window.configure(bg="#FFD700")  # Gold

title_font = ("Comic Sans MS", 30, "bold")
normal_font = ("Comic Sans MS", 18)

tk.Label(window, text="WELCOME TO MY FRUIT SHOP, HOW MAY I HELP YOU?", font=title_font, fg="navy", bg="#FFD700").pack(pady=20)

section = tk.StringVar()
options = [("A. I'm going to look and buy some fruits in this Shop.", "A"),
           ("B. I'm just going to look for the available fruits in this shop.", "B"),
           ("C. I'm going to look for the price of each available fruit in this shop.", "C"),
           ("D. I'm not going to buy or look for anything in this Online Fruit Shop.", "D")]

for text, value in options:
    tk.Radiobutton(window, text=text, variable=section, value=value, font=normal_font, bg="#FFD700").pack()

tk.Button(window, text="Submit", command=on_submit, font=normal_font, bg="#4CAF50", fg="white").pack(pady=20)

fruits = ["Apple", "Orange", "Watermelon", "Grapes", "Sweet Pomelo", "Papaya", "Banana", "Pineapple"]
selected_fruits = {fruit: tk.IntVar() for fruit in fruits}
quantities = {fruit: tk.IntVar(value=0) for fruit in fruits}
prices = {"Apple": 20, "Orange": 15, "Watermelon": 80, "Grapes": 80, "Sweet Pomelo": 50, "Papaya": 35, "Banana": 70, "Pineapple": 40}

window.mainloop()
