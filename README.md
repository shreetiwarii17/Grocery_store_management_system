# Grocery Store Management System

| | |
| :--- | :--- |
| **Name** | Shree Tiwari |
| **Section** | J |
| **Roll Number** | 00786 |

---

## Description

A console-based billing and inventory management application built in **Python 3**. It lets a cashier enter grocery items for a customer, checks that enough stock is available, automatically applies the discount and GST rules, reduces the stock, and saves every bill and the updated stock to text files.

### Concepts Used
* **Dictionaries:** `inventory` stores each product name with its unit price and available stock (`[price, stock]`).
* **Lists:** `cart` holds the items added to the current customer's bill.
* **Control Flow:** `while` and `for` loops with `if-elif-else` conditions for the menu, item entry and input validation.
* **File Handling:** Every finalized bill is appended to `bills.txt` (`"a"` mode) and the updated stock is saved to `stock.txt` (`"w"` mode).

### Inventory & Business Rules

| Item | Unit Price | Initial Stock |
| :--- | :--- | :--- |
| **Rice** | Rs. 50 / kg | 100 |
| **Sugar** | Rs. 45 / kg | 50 |
| **Milk** | Rs. 30 / L | 40 |
| **Oil** | Rs. 150 / L | 20 |

* **Discount Rule:** 10% discount if the subtotal is **Rs. 1,000 or more**.
* **Tax Rule:** 5% GST on the amount after discount.
* **Stock Validation:** Rejects items that do not exist, invalid quantities, and quantities greater than the available stock (including items already added to the current bill).
* **Note:** The program starts from the initial stock above every time it is run. `stock.txt` records the stock after each bill.

---

## How to Run

### Requirements
* **Python 3.6 or above** (download from [python.org](https://www.python.org/downloads/)).
* **No external libraries are needed.** The project uses only built-in Python features, so there is nothing to `pip install`.

### Steps
1. Check that Python 3 is installed:
   ```bash
   python --version
   ```
2. Download this project and open a terminal in the project folder.
3. Run the program:
   ```bash
   python code.py
   ```
4. Use the menu: `1` for a new bill, `2` to view stock, `3` to exit. While billing, enter an item name and quantity, and type `done` when finished.

### Files
* `code.py` – the program.
* `bills.txt` – every finalized bill is appended here.
* `stock.txt` – updated stock is saved here after each bill (format: `item,price,stock`).
* `summary.md` – project report with test cases.

---

## Sample Input and Output

### Test 1: Normal bill (no discount)
**Input**
```
1
Item: Rice
Quantity: 2
Item: Milk
Quantity: 3
Item: done
```
**Output**
```
Subtotal: 190.00 | Discount: 0.00
GST (5%): 9.50 | Total: Rs. 199.50
```

### Test 2: Boundary bill (discount applies at exactly Rs. 1000)
**Input**
```
1
Item: Oil
Quantity: 4
Item: Rice
Quantity: 8
Item: done
```
**Output**
```
Subtotal: 1000.00 | Discount (10%): 100.00
GST (5%): 45.00 | Total: Rs. 945.00
```

### Test 3: Invalid input
**Input**
```
1
Item: Butter
Quantity: 2
Item: Milk
Quantity: 50
Item: done
```
**Output**
```
Item 'Butter' not found in inventory.
Insufficient stock for Milk. Available: 40
No items in the cart. Bill not generated.
```

### Test 4: Stock deduction
**Input**
```
1
Item: Sugar
Quantity: 10
Item: Milk
Quantity: 5
Item: done
2
```
**Output**
```
Subtotal: 600.00 | Discount: 0.00
GST (5%): 30.00 | Total: Rs. 630.00
Rice: 100 | Sugar: 40 | Milk: 35 | Oil: 20
```

### Screenshots
<!-- Save your screenshots in a "screenshots" folder, then uncomment and edit: -->
<!-- ![Menu](screenshots/menu.png) -->
<!-- ![Bill](screenshots/bill.png) -->
