import json


def calculate_total_sales(product_file, sales_file):
    """
    Calculates total sales, handling both dictionary and
    list-of-dictionaries JSON formats.
    """

    try:
        with open(product_file, 'r') as f:
            products_data = json.load(f)

        with open(sales_file, 'r') as f:
            sales_data_1 = json.load(f)

    except FileNotFoundError:
        return "Error: One or both files not found."
    except json.JSONDecodeError:
        return "Error: Invalid JSON format in one or both files."

    products = {}  # Initialize as an empty dictionary
    sales = {}      # Initialize as an empty dictionary

    # Handle both dictionary and list formats for products
    if isinstance(products_data, dict):
        products = products_data
    elif isinstance(products_data, list):
        for product in products_data:
            products[product["title"]] = product["price"]
    else:
        return "Error: Invalid product data format."

    # Handle both dictionary and list formats for sales
    if isinstance(sales_data_1, dict):
        sales = sales_data_1
    elif isinstance(sales_data_1, list):
        for sale in sales_data_1:
            sales[sale["Product"]] = sale["Quantity"]
    else:
        return "Error: Invalid sales data format."

    total_sales = {}

    for product_name, price in products.items():
        if product_name in sales:
            quantity = sales[product_name]
            try:
                total_sales[product_name] = price * quantity
            except TypeError:
                return f"Error: Price or quantity for {product_name} is not a number."
        else:
            print(f"Warning: Product '{product_name}' found in product file but not in sales file.")

    for product_name, quantity in sales.items():
        if product_name not in products:
            print(f"Warning: Product '{product_name}' found in sales file but not in products file.")

    return total_sales


# Example usage:
product_file_path = "TC1.ProductList.json"
sales_file_path = "TC2.Sales.json"

sales_data = calculate_total_sales(product_file_path, sales_file_path)

if isinstance(sales_data, dict):
    total_revenue = sum(sales_data.values())
    print(f"Total Revenue: {total_revenue}")
elif isinstance(sales_data, str):
    print(sales_data)
else:
    print("An unexpected error occurred.")

with open("SalesResults.txt", "w") as results_file:
    results_file.write(f"Total sales cost: {total_revenue}\n")
