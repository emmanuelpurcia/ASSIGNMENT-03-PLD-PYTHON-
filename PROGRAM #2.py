import tkinter as tk
from tkinter import messagebox

class GroceryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python's Online Grocery App")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        # Fonts
        self.title_font = ("Arial", 18, "bold")
        self.label_font = ("Arial", 12)
        self.button_font = ("Arial", 12)

        # Variables
        self.money_var = tk.StringVar()
        self.products_var = []
        self.product_quantities = {}
        self.available_products = {
            "Apple": 20,
            "Mango": 30,
            "Orange": 15,
            "Watermelon": 50,
            "Pineapple": 40
        }
        self.selected_products = {}

        self.show_section1()

    def show_section1(self):
        self.clear_screen()

        self.label1 = tk.Label(self.root, text="PYTHON'S ONLINE GROCERY APP", font=self.title_font, fg="green")
        self.label1.pack(pady=30)

        self.next_button1 = tk.Button(self.root, text="Next", command=self.show_section2, font=self.button_font, bg="green", fg="white")
        self.next_button1.pack()

    def show_section2(self):
        self.clear_screen()

        self.label2 = tk.Label(self.root, text="Enter the amount of money you have (in peso format):", font=self.label_font)
        self.label2.pack(pady=20)

        self.money_entry = tk.Entry(self.root, textvariable=self.money_var, font=self.label_font)
        self.money_entry.pack()

        self.next_button2 = tk.Button(self.root, text="Next", command=self.show_section3, font=self.button_font, bg="green", fg="white")
        self.next_button2.pack()

    def show_section3(self):
        self.clear_screen()

        self.label3 = tk.Label(self.root, text="Select the products you want to buy:", font=self.label_font)
        self.label3.pack(pady=10)

        for product, price in self.available_products.items():
            var = tk.IntVar()
            self.products_var.append(var)
            checkbox = tk.Checkbutton(self.root, text=f"{product} ({price} pesos each)", variable=var, font=self.label_font)
            checkbox.pack()

        self.next_button3 = tk.Button(self.root, text="Next", command=self.show_section4, font=self.button_font, bg="green", fg="white")
        self.next_button3.pack()

    def show_section4(self):
        self.clear_screen()

        total_cost = 0
        remaining_money = 0
        selected_product = ""

        for i, (product, price) in enumerate(self.available_products.items()):
            if self.products_var[i].get() == 1:
                quantity = min(int(self.money_var.get()) // price, self.available_products[product])
                total_cost += quantity * price
                remaining_money = float(self.money_var.get()) - total_cost
                selected_product = product
                self.selected_products[product] = quantity

                self.label4 = tk.Label(self.root, text=f"Maximum {product} you can buy: {quantity}\nRemaining Money: {remaining_money:.2f} pesos", font=self.label_font)
                self.label4.pack(pady=20)

        self.buy_button = tk.Button(self.root, text="Buy", command=self.show_receipt, font=self.button_font, bg="green", fg="white")
        self.buy_button.pack()

        self.no_button = tk.Button(self.root, text="No", command=self.show_apology, font=self.button_font, bg="red", fg="white")
        self.no_button.pack()

    def show_receipt(self):
        self.clear_screen()

        total_cost = 0

        receipt_text = "Receipt:\n\n"
        for product, quantity in self.selected_products.items():
            price = self.available_products[product]
            total_cost += quantity * price
            receipt_text += f"{product} x{quantity} - {price * quantity:.2f} pesos\n"

        remaining_money = float(self.money_var.get()) - total_cost

        receipt_text += f"\nTotal Cost: {total_cost:.2f} pesos\nRemaining Money: {remaining_money:.2f} pesos"

        self.receipt_label = tk.Label(self.root, text=receipt_text, font=self.label_font)
        self.receipt_label.pack()

        self.ok_button = tk.Button(self.root, text="Ok", command=self.show_thank_you, font=self.button_font, bg="blue", fg="white")
        self.ok_button.pack()

    def show_apology(self):
        self.clear_screen()

        self.apology_label = tk.Label(self.root, text="We're sorry for not meeting your expectations. Have a great day, Customer!!", font=self.label_font, fg="red")
        self.apology_label.pack()

        self.ok_button = tk.Button(self.root, text="Ok", command=self.root.destroy, font=self.button_font, bg="blue", fg="white")
        self.ok_button.pack()

    def show_thank_you(self):
        self.clear_screen()

        self.thank_you_label = tk.Label(self.root, text="Thank you for visiting our Online Store, Have a Great Day Ahead!!", font=self.label_font, fg="green")
        self.thank_you_label.pack()

        self.ok_button = tk.Button(self.root, text="Welcome", command=self.root.destroy, font=self.button_font, bg="blue", fg="white")
        self.ok_button.pack()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = GroceryApp(root)
    root.mainloop()
