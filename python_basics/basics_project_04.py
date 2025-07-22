# project : Voting Eligibility System 

age=int(input("enter your age :" ))
nationality=input("enter your nationality : ")
voter_id=input("do you have a voter ID? (True/False) : ")

if age >= 18 and (nationality=="Indian" or nationality=="indian") and voter_id== True:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")