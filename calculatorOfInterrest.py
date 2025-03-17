#calculator with while loop

principle = 0;
time = 0;
interest=0;
#for principle
while principle <=0:
    principle = float(input("Enter your principle : "))
    if principle <=0:
     print ("Principle can not be zero or negtaive")    

#for time
while time <=0:
    time = float(input("Enter your time in years : "))
    if time <=0:
     print ("Time can not be zero or negtaive")    

#for interest
while interest <=0:
    interest = float(input("Enter your interest: "))
    if interest <=0:
     print ("interest can not be zero or negtaive")

print(principle)
print(time)        
print(interest)

total_interest= principle*time*(interest/100)
print(f"Total interest after {time} years {total_interest}")
total_money=principle+total_interest

print(f"Total amount after {interest}% interest in {time} years is {total_money : .2f} tk")





