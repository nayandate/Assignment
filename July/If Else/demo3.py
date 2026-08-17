'''
3. Character Occurrence Checker in Product Review

An e-commerce website wants to know how many times a particular character appears in a product review.

Input: Enter product review: this product is really good
       Enter character to check: o

Output: Character 'o' occurs: 4 times
'''

review = input("Enter product review: ")
check = input("Enter character to check: ")
count = 0
for ch in review:
       if ch == check:
           count+=1
print("Character '",check,"' occurs:",count,"times")
