import random

rounds=int(input("How Many Rounds You Want To Play : "))

option=["rock","paper","scissor"]
win = {
    "rock": "scissor",
    "scissor": "paper",
    "paper": "rock"
}
com_win=0
user_win=0
tie=0
for i in range(rounds):
    user=input("Enter Your Choice (Rock,Paper,Scissor) : ").lower()
    if user in option:
        computer=random.choice(option)
        print("Computer Choice : ",computer)
        if(user==computer):
            print("It's a Tie")
            tie+=1
        elif(win[user]==computer):
            user_win+=1
            print("You Win")
        else:
            com_win+=1
            print("Computer Win")
    else:
        print("Invalid Input")
print("Final Scores -> You :", user_win, "| Computer :", com_win, "| Tie :", tie)
if(user_win>com_win):
    print("Overall You Win")
elif(user_win==com_win):
    print("Overall It's a Tie")
else:
    print("Overall Computer Win")
