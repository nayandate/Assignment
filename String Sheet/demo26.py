'''
26. Find the first occurrence of a word. 
S = "Test this test", 
Word = "test" 10 (index)
'''

s = input("String: ")
word = input("Word: ")

index = s.find(word)

if index == -1:
    print("Word not found")
else:
    print("First occurrence:", index)