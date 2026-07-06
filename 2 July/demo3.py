'''
3. Prime Number Range Checker

A cyber security system generates prime numbers for encryption analysis.
The user enters a starting number and ending number.
The system checks and displays all prime numbers between the given range using nested loops.

Input:
Enter starting number: 10
Enter ending number: 50

Output:
Prime Numbers are:
11
13
17
19
23
29
31
37
41
43
47
'''

st = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
print("Prime Numbers are:")

for i in range(st, end + 1):
    count = 0

    if i > 1:
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                count += 1

        if count == 0:
            print(i)

