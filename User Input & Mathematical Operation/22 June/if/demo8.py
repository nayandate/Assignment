'''
8. Number Property Checker
   A system evaluates number properties:

* If number % 2 == 0 → Even number
* If number % 5 == 0 → Divisible by 5

Input:
Enter number: 20

Output:
Even number
Divisible by 5
'''
no = int(input("Enter number: "))

if no%2 == 0 :
    print("Even number")
else :
    print("Odd number")
if no%5 == 0 : 
    print("Divisible by 5")