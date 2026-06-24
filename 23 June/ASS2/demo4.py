'''
4. E-Learning Course Access System

An online learning platform grants access based on subscription type, course progress, and test score.

If subscription is premium, then check progress. If progress is at least 80, then check test score. If score is at least 70, unlock certificate; otherwise allow retry. If progress is less than 80, ask to complete course. If subscription is basic, then check progress. If progress is at least 50, allow limited access; otherwise lock content. If subscription is neither, deny access.

Input:
Subscription = premium
Progress = 85
Test Score = 65

Output:
Access Status = Retry Test
'''

sub = input("Subscription = ").lower()
prog = int(input("Progress = "))
ts = int(input("Test Score = "))

if sub == "premium":
     if prog >= 80:
          if ts>=70:
              print("Unlocked Certificate")
          else:
              print("Retry Test")
     else:
          print("Complete the remaining course")
elif sub == "basic":
    if prog >= 50:    
          print("Limited Access")
    else:
          print("Content is locked")
else:
    print("Access Denied")