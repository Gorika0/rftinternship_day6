import csv

# Read CSV file
with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)

    sales_per_product = {}
    total_revenue = 0

    print("Product-wise Sales:\n")

    for row in reader:
        product = row["PRODUCT"]
        quantity = int(row["QUANTITY"])
        price = int(row["PRICE"])

        # New column: TOTAL
        total = quantity * price

        # Add revenue
        total_revenue += total

        # Sales per product
        if product in sales_per_product:
            sales_per_product[product] += total
        else:
            sales_per_product[product] = total

        print(f"{product} -> Quantity: {quantity}, Price: {price}, Total: {total}")

# Sort by revenue
sorted_sales = sorted(
    sales_per_product.items(),
    key=lambda x: x[1],
    reverse=True
)

print("\nTotal Sales Per Product:")
for product, revenue in sorted_sales:
    print(f"{product}: {revenue}")

# Top-selling product
top_product = max(sales_per_product, key=sales_per_product.get)

print("\nTotal Revenue:", total_revenue)
print("Top-Selling Product:", top_product)
