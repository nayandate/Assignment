'''
6. Find Occurrence of a Word in a String

Product Review Analysis System

An e-commerce company wants to analyze customer reviews.

The company wants a Python program to count how many times a particular word appears in a review.

Input Sentence: iphone is good and iphone battery is strong

Word: iphone
Output: 2
'''

msg = input("Input: ")
word = input("Word: ")
x = msg.split()
count = 0
j=0
while j < len(x):
    if x == msg:
        count += 1
    j+=1
print(count)
