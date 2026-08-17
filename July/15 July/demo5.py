'''
5. Website URL Verification System

A software company is developing an automated website registration
portal. Before saving a website address, the system must verify whether
the URL follows the required company format.

Conditions: - Must start with www - Must end with .com

Input: Enter website: www.amazon.com

Output: Valid Website
'''

web = input("Enter website: ").lower()
x=0
i = 0
while i<len(web):
    if web[:4] == "www." and web[-4:] == ".com":
         if web[i] >= "a" and web[i] <= "z" and web[i] >= "0" and web[i] <= "9":
             x = 1
         else:
             print("Not a Valid Website")
             break
    else:
            print("Not a Valid Website")
            break
    i+=1
if x == 1:
     print("Valid Website")