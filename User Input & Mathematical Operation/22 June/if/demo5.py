'''
5. Banking Security System
   A bank validates login attempt:

* If username is "admin" → Valid user
* If password length ≥ 8 → Strong password

Input:
Enter username: admin
Enter password: secure123

Output:
Valid user
Strong password
'''

um = input("Enter username : ")
pw = input("Enter password : ")

if um == "admin" :
    print ("Valid user")

if pw == "secure123" :
    print ("Strong password")