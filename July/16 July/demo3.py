'''
3. Find the First Non-Repeated Character

Railway Ticket Fraud Detection System

The railway department generates ticket reference IDs automatically.

Sometimes, due to technical issues, many characters get repeated inside the ticket ID.

The department wants a Python program that finds the first character that appears only once in the string.

Example 1

Input:
aabbccddefg
Output:
e
'''

msg = input("Input: ")

i = 0
while i<len(msg):
     count=0
     j = 0
     while j<len(msg):
         if msg[i]==msg[j]:
             count+=1
         j+=1
     if count == 1:
          print("Output:",msg[i])
          break
     i += 1