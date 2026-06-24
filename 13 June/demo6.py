#You insert an amount into a vending machine. It returns coins using the largest denominations possible (₹10 and ₹5).


ammo=int(input("Enter the amount"))
ten=ammo//10
rem=ammo%10
five=rem//5

print("₹10 x {}, ₹5 x {}".format(ten,five))