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

sub = input("Subscription = ")
pro = int(input("Progress = "))
tsc = int(input("Test Score = "))

if sub.lower()== "premium":
        if pro>=80:
            if tsc>=70:
                print("Access Status = Unlocked Cerificate")
            else:
                print("Access Status = Retry Test")
        else:
            print("Complete Remaining Course")
elif sub.lower()== "basic":
        if pro>=50:
            print("Access Status = Limited")
        else:
            print("Content Locked")
else:
      print("Access Denied")