
products = {}
while True:
      product_name = input("Enter the product name (or 'done' to finish): ")
      if product_name.lower() == 'done':
        break
      
      product_price = (input(f"Enter the price for {product_name}: "))
      # Check if the price is a valid number
      if product_price.replace('.', '', 1).isdigit():
        products[product_name] = float(product_price)
      else:
        print("Please enter a valid price.")      


while True:
    find = input("Enter a product name to get its price (or 'done' to finish): ")
    if find.lower() == 'done':
        break
    if find in products:
        print(f"The price of {find} is {products[find]}")
    else:
        print(f"{find} is not in the product list.")
        


















