'''
1. Utility Toolkit System

You are developing a Utility Toolkit Application for a small office. Employees use this tool to quickly perform common number operations like checking prime numbers, reversing numbers, etc.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Check Prime Number
2 → Check Palindrome Number
3 → Reverse a Number
4 → Count Digits
5 → Exit

Sample Run 1:
Input:
Enter your choice: 1
Enter number: 7

Output:
7 is a Prime Number

Sample Run 2:
Input:
Enter your choice: 2
Enter number: 121

Output:
121 is a Palindrome Number

Sample Run 3:
Input:
Enter your choice: 3
Enter number: 456

Output:
Reversed Number is: 654

Sample Run 4:
Input:
Enter your choice: 4
Enter number: 98765

Output:
Total digits: 5

Sample Run 5 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

Sample Run 6 (Exit):
Input:
Enter your choice: 5

Output:
Exiting program... Thank you!

Requirements:

* Use while loop to repeat menu
* Use match-case for decision making
* Handle negative numbers properly
* Use only loops and conditions
'''

while True:
   print("\n1 → Check Prime Number")
   print("2 → Check Palindrome Number")
   print("3 → Reverse a Number")
   print("4 → Count Digits")
   print("5 → EXIT")

   ch = int(input("\nEnter your choice : "))
   match ch:
      case 1:
            n = int(input("Enter Number : "))
            if n < 2:
               print(n,"is not Prime")
            else:
               i = 2
               while i <= n//2:
                  if n % i == 0:
                     print(n,"is not prime")
                     break
                  i+=1
               else:
                  print(n,"is Prime Number")

      case 2: 
            n = int(input("Enter Number : "))
            rem = 0
            no = n
            while n>0:
                rem = n%10+rem*10
                n=n//10
            if rem == no:
                print(no,"is Palindrome number")
            else:
                print(no,"is not a Palindrome number")
            
      case 3: 
            n = int(input("Enter Number : "))
            rem = 0
            while n>0:
                rem = n%10+rem*10
                n=n//10
            print(rem,"is Reverse Number")

      case 4:
            n = int(input("Enter Number : "))
            count = 0
            while n>0:
                count+=1
                n=n//10
            print(count,"is Total digits")

      case 5:
            print("Exiting program... Thank you!")
            break
      
      case __:
            print("Invalid Choice")
