from models.product import Product

def read_product(index):
    product_id, product_name, price, quantity = input(
        f"Enter details for product {index}: "
    ).split()
    return Product(
        int(product_id),
        product_name,
        int(price),
        int(quantity),
    )


def main():
    products = [read_product(index) for index in range(1, 6)]

    print("\nAll Products:")
    for product in products:
        print(product)

    print("\nProduct Total Values:")
    for product in products:
        print(f"{product.product_name} = {product.total_value()}")

    print("\nLow Stock Products:")
    for product in products:
        if product.quantity < 10:
            print(product.product_name)

    highest_price_product = max(products, key=lambda product: product.price)
    print("\nHighest Price Product:")
    print(
        f"{highest_price_product.product_name} = "
        f"{highest_price_product.price}"
    )

    total_inventory_value = sum(product.total_value() for product in products)
    print("\nTotal Inventory Value:")
    print(total_inventory_value)

    search_id = int(input("\nSearch Product Id: "))
    found_product = next(
        (product for product in products if product.product_id == search_id),
        None,
    )

    print("\nProduct Found:")
    if found_product is not None:
        print(found_product)
    else:
        print("Product not found")


if __name__ == "__main__":
    main()