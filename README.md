# Grocery Store Management System

A console-based billing and inventory management application built in **Python 3**. This program allows a cashier to select grocery items, validate stock availability, automatically calculate discounts and GST, update inventory levels, and save itemized receipts to a text file.

---

## Concepts Used
* **Dictionaries:** Store product names, unit prices, and available stock quantities.
* **Lists:** Manage items added to the active customer shopping cart.
* **Control Flow:** `while` and `for` loops with `if-elif-else` conditions for menu navigation and input validation.
* **File Handling:** Appends every finalized receipt to `bills.txt` (`"a"` mode) and updates inventory counts in `stock.txt` (`"w"` mode).

---

## Initial Inventory & Business Rules

| Item | Unit Price | Initial Stock |
| :--- | :--- | :--- |
| **Rice** | Rs. 50 / kg | 100 kg |
| **Sugar** | Rs. 45 / kg | 50 kg |
| **Milk** | Rs. 30 / L | 40 L |
| **Oil** | Rs. 150 / L | 20 L |

* **Discount Rule:** A **10% discount** is applied automatically if the subtotal is **Rs. 1,000 or more**.
* **Tax Rule:** **5% GST** is calculated on the amount after discount.
* **Stock Validation:** Prevents billing non-existent items or quantities exceeding available stock.

---

## How to Run

1. Make sure **Python 3** is installed on your system.
2. Clone or download this repository and open a terminal in the project folder.
3. Run the application:
   ```bash
   python grocery_billing.py