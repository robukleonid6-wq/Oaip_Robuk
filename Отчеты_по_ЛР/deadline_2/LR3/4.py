products = {
    "ноутбук": {"price": 50000, "sold": 15},
    "мышь": {"price": 1000, "sold": 45},
    "клавиатура": {"price": 2500, "sold": 30},
    "монитор": {"price": 30000, "sold": 8}
}

max_sold = 0
best_selling_product = ""
for product, info in products.items():
    if info["sold"] > max_sold:
        max_sold = info["sold"]
        best_selling_product = product

print(f"самый продаваемый товар: {best_selling_product} ({max_sold} колл-во)")

total_revenue = 0
for product, info in products.items():
    revenue = info["price"] * info["sold"]
    total_revenue += revenue

print(f"общая выручка {total_revenue} руб.")

max_revenue = 0
best_revenue_product = ""
for product, info in products.items():
    revenue = info["price"] * info["sold"]
    if revenue > max_revenue:
        max_revenue = revenue
        best_revenue_product = product

print(f"товар с наибольшей выручкой {best_revenue_product} ({max_revenue} руб.)")