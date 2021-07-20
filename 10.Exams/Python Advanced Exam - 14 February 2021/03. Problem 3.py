def stock_availability(*args):
    result = []
    for el in args:
        result.append(el)

    all_products = []
    for el in result[0]:
        all_products.append(el)

    if "delivery" in result:
        idx_of_command = result.index("delivery")

        new_product = result[idx_of_command + 1::]
        for el in new_product:
            all_products.append(el)

    elif "sell" in result:
        idx_of_command = result.index("sell")
        product_to_remove = result[idx_of_command + 1::]

        product_num = None
        for i in product_to_remove:
            if str(i).isnumeric():
                product_num = int(i)

        if not product_to_remove:
            all_products.pop(0)

        if product_num:
            for i in range(int(product_num)):
                all_products.pop()

        elif product_to_remove:
            product_to_remove = []
            for el in result[idx_of_command + 1::]:
                product_to_remove.append(el)
            for el in product_to_remove:
                for i in range(len(all_products)):
                    if el in all_products:
                        all_products.remove(el)
    return all_products


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
