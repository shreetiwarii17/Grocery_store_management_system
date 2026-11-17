# Grocery Store Management System

| | |
| :--- | :--- |
| **Name** | Shree Tiwari |
| **Class / Section** | J |
| **Roll Number** | 00786 |

---

## Description

A console-based billing and inventory management application built in **Python 3**. It lets a cashier select grocery items, validates stock availability, automatically calculates discounts and GST, updates inventory levels, and saves itemized receipts to a text file.

### Concepts Used
* **Dictionaries:** Store product names, unit prices, and available stock quantities.
* **Lists:** Manage items added to the active customer shopping cart.
* **Control Flow:** `while` and `for` loops with `if-elif-else` conditions for menu navigation and input validation.
* **File Handling:** Appends every finalized receipt to `bills.txt` (`"a"` mode) and updates inventory counts in `stock.txt` (`"w"` mode).

### Initial Inventory & Business Rules

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

### Requirements
* **Python 3.x** (download from [python.org](https://www.python.org/downloads/))
* **No external libraries needed.** The project uses only Python's built-in features, so there is nothing to `pip install`.

### Steps
1. Make sure Python 3 is installed. Check with:
   ```bash
   python --version
   ```
2. Clone or download this repository and open a terminal in the project folder.
3. Run the application:
   ```bash
   python grocery_billing.py
   ```
4. Follow the on-screen prompts to add items to the cart and generate the bill.

### Output Files
* `bills.txt` – every finalized receipt is appended here.
* `stock.txt` – updated inventory counts are saved here after each sale.

---

## Sample Input and Output

> Replace this section with your own screenshots or a copy of your actual program output.

### Sample Input
```
Item: Rice      Quantity: 10
Item: Oil       Quantity: 4
```

### Sample Output
```
------------- RECEIPT -------------
Rice   10 kg  x  Rs. 50   = Rs. 500.00
Oil     4 L   x  Rs. 150  = Rs. 600.00
-----------------------------------
Subtotal            : Rs. 1100.00
Discount (10%)      : Rs. 110.00
After Discount      : Rs. 990.00
GST (5%)            : Rs. 49.50
Total Payable       : Rs. 1039.50
-----------------------------------
```