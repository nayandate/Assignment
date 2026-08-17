'''
3.  Smart Chat Message Cleaner

A social media company noticed that users often enter messages with unnecessary spaces. To improve readability and storage efficiency, the system should remove extra spaces 
and keep only a single space between words.

Input: Enter message: Java is easy

Output: Cleaned Message: Java is easy
'''

msg = input("Enter message: ")
result=""

i=0
while i<len(msg):
      if (msg[i]!=" ") :
          result+= msg[i]
          x = 0
      else:
          if result!="" and x == 0:
             result+= " "
             x=1
      i+=1
if len(result) > 0 and result[-1] == " ":
    result = result[:-1]

print("Cleaned Message:",result)