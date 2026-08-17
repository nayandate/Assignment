'''
27. Find the last occurrence of a word. 
S = "Test this test", 
Word = "test" 
15 (index)
'''

s = input("String: ")
word = input("Word: ")

index = s.rfind(word)

if index == -1:
    print("Word not found")
else:
    print("First occurrence:", index)