'''
6. Railway Ticket PNR Analyzer

A railway department wants to verify whether a PNR number is valid.

Conditions:
- PNR must start with "PNR"
- Total length should be 12 characters
- Remaining characters should be digits

Input:
Enter PNR: PNR123456789

Output:
Valid PNR Number
'''

pnr = input("Enter PNR: ")
length = len(pnr)
count = 0

if length == 12:
     if pnr[0] == "P" and pnr[1] == "N" and pnr[2] == "R":
        i = 3
        while i<length:
              if pnr[i] >= "0" and pnr[i] <= "9":
                   count+=1
              i+=1

if count == 9:
    print("Valid PNR Number")
else:
    print("Not Valid PNR Number")