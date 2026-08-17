'''
6.
NOTE: using tuple only
An electronics store wants to maintain product information. Since product details should not be modified accidentally,
 each product record is stored as a tuple.

Tuple Format:

(product_id, product_name, price)

Requirements:

Read N product details from the user and store them as tuples in a list.
Display all product details.
Find and display the costliest product.
Find and display the cheapest product.
Calculate and display the average price of all products.
Display all products whose price is greater than ₹50,000.

Test Case:

Input:

Enter number of products: 4

P101 Laptop 65000
P102 Mobile 25000
P103 Television 80000
P104 Tablet 30000

Expected Output:

All Products:
('P101', 'Laptop', 65000)
('P102', 'Mobile', 25000)
('P103', 'Television', 80000)
('P104', 'Tablet', 30000)

Costliest Product:
('P103', 'Television', 80000)

Cheapest Product:
('P102', 'Mobile', 25000)

Average Price:
50000.0

Products Above ₹50,000:
('P101', 'Laptop', 65000)
('P103', 'Television', 80000)

'''

n = int(input("Enter number of Products:"))
products = []

for i in range(n):
    print("Enter Details:")
    id = input("Enter Book ID:")
    name = input("Enter Book Title:")
    price = int(input("Enter Price:"))
    x = (id,name,price)
    products.append(x)

for i in products:
    print(i)

print("Costliest Product:")

max = 0
min = products[0][2]
maxarr = []
minarr = []
for x in products:
    if x[2] > max:
        max = x[2]
        maxarr.append(x)
    if x[2] < min:
        min = x[2]
        minarr.append(x)
print(maxarr[-1])

print("Cheapest Product:")
print(minarr[-1])

print("Average Price")

avg = 0
for x in products:
    avg += x[2]
      
print(avg/len(products))

print("Products Above ₹50,000:")
for x in products:
    if x[2] > 50000:
        print(x)