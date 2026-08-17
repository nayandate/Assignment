'''
10. Online Exam System
    System evaluates exam conditions:

* If marks ≥ 40 → Pass
* If attendance ≥ 75 → Eligible for certificate

Input:
Enter marks: 60
Enter attendance: 80

Output:
Pass
Eligible for certificate
'''

mrk = int(input("Enter marks: "))
atd = int(input("Enter attendance: "))

if mrk>=40 :
    print ("Pass")

if atd>=75 :
    print ("Eligible for certificate")