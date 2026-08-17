#A bank wants to help customers calculate the simple interest on their savings.


p,r,t=map(float,input("Enter the principal amount, rate of interest, and time (in years) seperate them by space:").split())
si=(p*r*t)/100
print("Principal ={}\nRate = {}\nTime = {}\nSimple Interest = {}".format(p,r,t,si))