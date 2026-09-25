from models.customer import Customer


def read_customers(count):
    customers = []

    for number in range(1, count + 1):
        print(f"Enter details for customer {number} (id name city purchase_amount):")
        customer_id, customer_name, city, purchase_amount = input().split()
        customers.append(
            Customer(
                int(customer_id),
                customer_name,
                city,
                float(purchase_amount),
            )
        )

    return customers


def display_customers(customers, include_city=False):
    for customer in customers:
        if include_city:
            print(customer)
        else:
            print(
                f"{customer.customer_id} {customer.customer_name} "
                f"{customer.purchase_amount:g}"
            )


def main():
    customers = read_customers(5)

    print("\nAll Customers:")
    display_customers(customers)

    city = input("\nEnter city to display: ").strip()
    print(f"\nCustomers from {city}:")
    display_customers(
        [customer for customer in customers if customer.city.lower() == city.lower()]
    )

    print("\nCustomers with purchase amount greater than 10000:")
    display_customers(
        [customer for customer in customers if customer.purchase_amount > 10000]
    )

    highest_purchase_customer = max(
        customers, key=lambda customer: customer.purchase_amount
    )
    print("\nHighest Purchase Customer:")
    display_customers([highest_purchase_customer])

    total_sales = sum(customer.purchase_amount for customer in customers)
    average_purchase = total_sales / len(customers)
    print("\nTotal Sales:")
    print(f"{total_sales:g}")
    print("\nAverage Purchase Amount:")
    print(f"{average_purchase:g}")

    customer_id = int(input("\nSearch Customer Id: "))
    found_customer = next(
        (customer for customer in customers if customer.customer_id == customer_id),
        None,
    )
    print("\nCustomer Found:")
    if found_customer:
        print(found_customer)
    else:
        print("Customer not found")


if __name__ == "__main__":
    main()
