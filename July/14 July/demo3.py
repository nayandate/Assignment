'''
3. Word Counter in Complaint Message

A customer care system wants to count how many words are present in a complaint message.

Input:
Enter complaint: Delivery was delayed again today

Output:
Total words: 5
'''
'''
1.

a = input("Enter complaint: ")

count = 0

for i in range(len(a)):
    if a[i] != " " and (i == 0 or a[i-1] == " "):
        count += 1

print("Total words:", count)
'''


word = input("Enter complaint: ")
length = len(word)
count = 0
i = 0
while(i<length):
       if word[i] != " ":
           count += 1
           while i < length and word[i] != " ":
               i += 1
       else:
           i += 1
print("Total words: ",count)
