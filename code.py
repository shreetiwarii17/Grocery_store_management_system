inventory = {
    "Rice": [50, 100],
    "Sugar": [45, 50],
    "Milk": [30, 40],
    "Oil": [150, 20]
}


def save_stock():
    """Saves the updated stock into stock.txt"""
    file = open("stock.txt", "w")
    for item in inventory:
        file.write(item + "," + str(inventory[item][0]) + "," + str(inventory[item][1]) + "\n")
    file.close()


def view_stock():
    """Displays the current stock"""
    line = ""
    for item in inventory:
        line = line + item + ": " + str(inventory[item][1]) + " | "
    print(line[:-3])


def new_bill():
    """Creates a bill, checks stock, calculates totals and saves files"""
    cart = []  # list of items in the current bill

    print("Type 'done' when finished adding items.")

    while True:
        item = input("Item: ").strip().capitalize()
        if item == "Done":
            break

        qty_text = input("Quantity: ")

        # Check that the item exists
        if item not in inventory:
            print("Item '" + item + "' not found in inventory.")
            continue

        # Check that the quantity is a valid number
        if not qty_text.isdigit() or int(qty_text) == 0:
            print("Please enter a valid quantity.")
            continue
        qty = int(qty_text)

        # Stock left after the items already in the cart
        available = inventory[item][1]
        for c in cart:
            if c[0] == item:
                available = available - c[1]

        # Check that the stock is enough
        if qty > available:
            print("Insufficient stock for " + item + ". Available: " + str(available))
            continue

        price = inventory[item][0]
        cart.append([item, qty, price, price * qty])

    if len(cart) == 0:
        print("No items in the cart. Bill not generated.")
        return

    # Subtotal
    subtotal = 0
    for c in cart:
        subtotal = subtotal + c[3]

    # Discount: 10% if subtotal is Rs. 1000 or more
    discount = 0
    if subtotal >= 1000:
        discount = subtotal * 0.10

    # GST: 5% on the amount after discount
    gst = (subtotal - discount) * 0.05
    total = subtotal - discount + gst

    # Print the bill
    if discount > 0:
        print(f"Subtotal: {subtotal:.2f} | Discount (10%): {discount:.2f}")
    else:
        print(f"Subtotal: {subtotal:.2f} | Discount: {discount:.2f}")
    print(f"GST (5%): {gst:.2f} | Total: Rs. {total:.2f}")

    # Reduce the stock after billing
    for c in cart:
        inventory[c[0]][1] = inventory[c[0]][1] - c[1]

    # Append the final bill to bills.txt
    file = open("bills.txt", "a")
    for c in cart:
        file.write(c[0] + " x " + str(c[1]) + " = " + f"{c[3]:.2f}" + "\n")
    file.write(f"Subtotal: {subtotal:.2f} | Discount: {discount:.2f}\n")
    file.write(f"GST (5%): {gst:.2f} | Total: Rs. {total:.2f}\n\n")
    file.close()

    # Save the updated stock
    save_stock()


# Main menu
while True:
    print("\n1. New bill")
    print("2. View stock")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        new_bill()
    elif choice == "2":
        view_stock()
    elif choice == "3":
        print("YAY, VISIT AGAIN~~")
        break
    else:
        print("Invalid choice. Enter 1, 2 or 3.")