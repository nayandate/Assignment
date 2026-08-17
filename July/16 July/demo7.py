'''
7. Remove Duplicate Words from a String

Voice Assistant Noise Correction System

A voice assistant records spoken commands from users.
Due to microphone disturbance and network lag, some words are repeated multiple times.
The company wants a Python program that removes duplicate words while maintaining the original order.

 Input: hello hello how are are you
Output: hello how are you
'''

msg = input("Input: ")
x = msg.split()
result=x[0]+" "

i=0
while i<len(x)-1:
    if x[i] != x[i+1]:
        result+=x[i+1]+" "
    i+=1
print("Output:",result)
