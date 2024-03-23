def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for inputs
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(original_price, discount_percent)

# Print the final price after applying the discount
if final_price != original_price:
    print("Final price after applying the discount: ${:.2f}".format(final_price))
else:
    print("No discount applied. Original price: ${:.2f}".format(original_price))
