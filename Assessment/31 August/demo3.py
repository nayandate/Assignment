'''

QUESTION 3: LIBRARY BOOK RECORD ANALYSIS(3 marks)

A library wants to maintain and analyze its book records using NamedTuple.

Each book contains the following information:

Fields:
book_id, title, author, price

Requirements:
Read N book records from the user and store them in a list of NamedTuple.
Display all book details.
Find and display the most expensive book.
Find and display the cheapest book.
Calculate and display the average price of all books.
Display all books whose price is greater than the average book price.
Test Case

Input:

Enter number of books: 6

Enter details for Book 1:
Enter Book ID: B201
Enter Title: C Programming
Enter Author: Robert
Enter Price: 400

Enter details for Book 2:
Enter Book ID: B202
Enter Title: Web Development
Enter Author: Martin
Enter Price: 650

Enter details for Book 3:
Enter Book ID: B203
Enter Title: Python Advanced
Enter Author: Robert
Enter Price: 800

Enter details for Book 4:
Enter Book ID: B204
Enter Title: Database Systems
Enter Author: Thomas
Enter Price: 500

Enter details for Book 5:
Enter Book ID: B205
Enter Title: Machine Learning
Enter Author: David
Enter Price: 900

Enter details for Book 6:
Enter Book ID: B206
Enter Title: Computer Networks
Enter Author: Martin
Enter Price: 350
Expected Output
All Book Details:
B201 C Programming Robert 400
B202 Web Development Martin 650
B203 Python Advanced Robert 800
B204 Database Systems Thomas 500
B205 Machine Learning David 900
B206 Computer Networks Martin 350

Most Expensive Book:
B205 Machine Learning David 900

Cheapest Book:
B206 Computer Networks Martin 350

Average Book Price:
600.0

Books With Price Greater Than Average:
B202 Web Development Martin 650
B203 Python Advanced Robert 800
B205 Machine Learning David 900
'''

from collections import namedtuple
Book = namedtuple("Book", ["book_id", "title", "author", "price"])
n = int(input("Enter number of books: "))

books = []
for i in range(n):
    print()
    print("Enter details for Book", i + 1)
    book_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    price = int(input("Enter Price: "))

    book = Book(book_id, title, author, price)
    books.append(book)

print()
print("All Book Details:")
for book in books:
    print(book.book_id, book.title, book.author, book.price)

print()
expensive = books[0]

for book in books:
    if book.price>expensive.price:
        expensive = book

print("Most Expensive Book:")
print(expensive.book_id, expensive.title, expensive.author, expensive.price)

print()
cheap = books[0]
for book in books:
    if book.price<cheap.price:
        cheap = book
print("Cheapest Book:")
print(cheap.book_id, cheap.title, cheap.author, cheap.price)

print()
total = 0
for book in books:
    total = total+book.price
average = total/n
print("Average Book Price:")
print(average)

print()
print("Books With Price Greater Than Average:")
for book in books:
    if book.price>average:
        print(book.book_id, book.title, book.author, book.price)