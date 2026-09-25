'''
3.
ONLINE SHOPPING SYSTEM
Scenario:
An e-commerce company wants to develop an Online Shopping System.
 The application should be menu-driven and should demonstrate different types of arguments used in Python functions.

MENU
1. Customer Registration
2. Product Information
3. Generate Invoice
4. Add Multiple Products
5. Display Customer Profile
6. Exit

Requirements
Choice 1 – Customer Registration

* Accept Customer Name, Email, and Mobile Number.
* Pass the values to a function using Positional Arguments.
* Display the registered customer details.

Choice 2 – Product Information
* Accept Product Name, Price, and Category.
* Call the function using Keyword Arguments.
* Display the product details.

Choice 3 – Generate Invoice

* Accept Product Name and Price.
* Tax Percentage should have a default value.
* Use Default Arguments while generating the invoice.
* Display the final amount.

Choice 4 – Add Multiple Products

* Allow the user to enter any number of product prices.
* Pass all prices to a function using Variable Length Arguments (*args).
* Calculate and display the total bill amount.

Choice 5 – Display Customer Profile

* Accept any number of customer details such as Name, City, Email, Mobile, Membership Type, etc.
* Pass the details using Arbitrary Keyword Arguments (**kwargs).
* Display all customer information.

Choice 6 – Exit

Sample Execution

Enter Choice : 1
Enter Name : Ajay
Enter Email : [ajay@gmail.com](mailto:ajay@gmail.com)
Enter Mobile : 9876543210

Customer Registered Successfully

---
Enter Choice : 2

Enter Product Name : Laptop
Enter Price : 55000
Enter Category : Electronics

Product Details Displayed Successfully
---

Enter Choice : 3

Enter Product Name : Laptop
Enter Price : 55000

Invoice Generated Successfully
---

Enter Choice : 4

Enter Number of Products : 4

Enter Price 1 : 100
Enter Price 2 : 200
Enter Price 3 : 300
Enter Price 4 : 400

Total Bill Amount : 1000
---

Enter Choice : 5

Customer Profile Displayed Successfully
---

Enter Choice : 6
Thank You. Program Terminated.

Important Instructions

1. Choice 1 must use Positional Arguments.
2. Choice 2 must use Keyword Arguments.
3. Choice 3 must use Default Arguments.
4. Choice 4 must use Variable Length Arguments (*args).
5. Choice 5 must use Arbitrary Keyword Arguments (**kwargs).
6. Use separate functions for each menu option.
7. Implement the solution using a menu-driven approach.
8. Maintain proper code readability and formatting.
'''

while True:
    print("""
1. Customer Registration
2. Product Information
3. Generate Invoice
4. Add Multiple Products
5. Display Customer Profile
6. Exit
""")
    ch = int(input("Enter Choice: "))
    match ch:

        case 1:
            def registration(name,email,no):
                print("Customer Name:",name)
                print("Customer Email:",email)
                print("Customer Mobile Number:",no)
                print()
                print("Customer Registered Successfully")

            name = input("Enter The Name:")
            email = input("Enter The Email:")
            no = int(input("Enter The Number:"))
            registration(name,email,no)

        case 2:
            def product(pname,price,category):
                print("Product Name:",pname)
                print("Product Price:",price)
                print("Product Category :",category)
                print()
                print("Product Details Displayed Successfully")
                              
            product_name = input("Enter Product Name :")
            price = int(input("Enter Price :"))
            Category = input("Enter Category :")
            product(pname = product_name,price = price,Category = Category)

        case 3:
            def invoice(pname,price,tax = 5):
                print("Product Name:",pname)
                print("Product Price:",price)
                final = price + price* (5/100)
                print("Final Price:",final)
                print("Invoice Generated Successfully")

            product_name = input("Enter Product Name :")
            price = int(input("Enter Price :"))

            invoice(product_name,price)

        case 4:
            def totalAmount(*pro):
                print("Total Bill Amount :",sum(pro))

            n = int(input("Enter Number Of Product:"))
            pro = []
            for i in range(n):
                temp = input(f"Enter Price {i+1} :")
                pro.append(temp)
            totalAmount(*pro)

        case 5:
            def custProfile(**profile):
                for k,v in profile.items():
                    print(k," : ",v)
                print("Customer Profile Displayed Successfully")

            name = input("Enter The Name:")
            email = input("Enter The Email:")
            no = int(input("Enter The Number:"))
            city = input("Enter The City:")
            custProfile(name = name,email = email,no = no,city = city)

        case 6:
            print("Thank You. Program Terminated.")
            break

        case __:
            print("Not a Valid Choice")