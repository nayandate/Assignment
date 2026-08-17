'''
4.  Instant Messaging Word Encryption System

A messaging application wants to temporarily encrypt messages during
transmission. The encryption rule is to reverse every word individually
while keeping the word positions unchanged.

Input: Enter message: java is powerful

Output: Encrypted Message: avaj si lufrewop
'''

msg = input("Enter message: ")
result = ""

i = 0
while i<len(msg):
     word=""
     
     while i<len(msg) and msg[i] != " ":
         word+= msg[i]
         i+=1

     j = len(word) - 1
     while j>=0:
          result+= word[j]
          j-=1

     if i < len(msg) and msg[i] == " ":
        result += " "
        i += 1

print("Encrypted Message:", result)