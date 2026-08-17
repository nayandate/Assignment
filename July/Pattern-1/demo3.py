'''
3. WAP to find out all the leap years between two entered years
'''

n = int(input("Enter start year to find out all the leap years: " ))
e = int(input("Enter end year to find out all the leap years: "))
i=n
while i<=e:
      if i % 4 == 0:
           if i%100 == 0:
                if i%400 == 0:
                    print(i," -> Leap Year")
                else:
                    print(i," -> Not Leap Year")
           else:
                print(i," -> Leap Year")
      else:
           print(i," -> Not Leap Year")
      i+=1

