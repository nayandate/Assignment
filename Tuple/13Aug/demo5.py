'''
QUESTION 5: LIBRARY BOOK RECORDS
================================
A library maintains book information using NamedTuple.
Fields:
book_id, title, author, price
Requirements:
1. Read N book records from the user and store them in a list of NamedTuples.
--
2. Display all book details.
---
3. Find and display the most expensive book.
---
4. Search books by author name.
--
5. Calculate and display the average price of all books.
---
Test Case:

Input:
Enter number of books: 4

B101 Python Basics John 450
B102 Java Programming James 550
B103 Data Science John 700
B104 SQL Guide Smith 300

Enter Author Name: John

Expected Output:
Most Expensive Book:
B103 Data Science John 700

Average Book Price:
500.0

Books Written By John:
B101 Python Basics John 450
B103 Data Science John 700
'''

from collections import namedtuple
Book = namedtuple("patient",["book_id", "title", "author", "price"])
n = int(input("Enter number of Books:"))
books = []
for i in range(n):
    print("Enter Details:")
    id = input("Enter Book ID:")
    title = input("Enter Book Title:")
    author = input("Enter Author Name:")
    price = int(input("Enter Price:"))
    p = Book(id,title,author,price)
    books.append(p)

auth = input("Enter Author Name:")

print(books)
print("details:")
for x in books:
    print(x.book_id,x.title,x.author,x.price)


print("Most Expensive Book:")

max = 0
ans = []
for x in books:
    if x.price > max:
        max = x.price
        ans.append(x)
print(ans[-1].book_id,ans[-1].title,ans[-1].author,ans[-1].price)



print("Average Book Price:")
avg = 0
for x in books:
    avg += x.price
      
print(avg/len(books))


print("Books Written By",auth,":")
for x in books:
    if x.author == auth:
        print(x.book_id,x.title,x.author,x.price)