class Customer:
    def __init__(self, customer_id, customer_name, city, purchase_amount):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.city = city
        self.purchase_amount = purchase_amount

    def __str__(self):
        return (
            f"{self.customer_id} {self.customer_name} {self.city} "
            f"{self.purchase_amount:g}"
        )
