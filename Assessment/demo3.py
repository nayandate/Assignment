'''
3. Reverse Sentence + Reverse Each Word(3 marks)

Secret Military Communication Decoder
A defense organization stores highly confidential messages in encrypted form.
To decode the message:

1. Reverse the entire sentence.
2. Reverse every individual word.
3. Store the final result back into the original string variable.

You must use the split() method.
Input: Python is powerful

Output: lufrewop si nohtyP
'''

msg = input("Input: ")
x = msg.split()
result=""

i = len(x)-1
while i>=0:
    word = x[i]

    j = len(word) -1
    while j>=0:
        result+=word[j]
        j-=1

    if i!=0:
         result+=" "
    i-=1

msg = result
print("Output:",msg)