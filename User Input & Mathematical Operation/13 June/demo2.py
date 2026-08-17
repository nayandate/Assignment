#You are developing a feature for a health and wellness mobile app that helps users understand how long they've been alive in a more tangible way.

age=int(input("Enter your age in years:"))
days=age * 365+ age//4
print("Days",days)
hours=age*365*24
print("Hours ",hours)
min=age*365*24*60
print("Min ",min)