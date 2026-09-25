'''
4. Assignment 10: Cyber Security (Strong Password Check)

A cybersecurity company considers a numeric password to be "strong" if every digit is even.

Task

Write a recursive function to check whether all digits of the given number are even.

Input 1
Enter Password:
248620
Output 1
Strong Password

Input 2
Enter Password:
248621
Output 2
Weak Password
'''

def even(num):
    if num == 0:
        return True
    check = num%10
    if check%2!=0:
        return False
    num=num//10
    return even(num)
num = (int(input("Enter Password: ")))
even(num)
if even(num) == True:
    print("Strong Password")
else:
    print("Weak Password")