'''
4. Program should work for both uppercase and lowercase letters.

Find the Shortest Word in a Sentence

Telecom SMS Cost Optimization System:
A telecom company charges customers based on the length of words used in bulk SMS campaigns.
The company wants to identify the shortest word in every message for analytics purposes.

Write a Python program to find the shortest word from a given sentence.
Input:
Python is very easy to learn
Output:
is
'''

msg = input("Input: ")
count = ""

i=0
while len(msg)>=i:
      word = ""
      while i<len(msg) and msg[i] != " ":
            word+= msg[i]
            i+=1
      if word != "":
            if len(count)>len(word) or count == "": 
                  count = word
      i+=1
print("Output:",count)