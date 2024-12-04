#Banking System
print("BANKING SYSTEM")
total_amt = 0
def withdraw(withdraw_amt):
    global total_amt
    if withdraw_amt > total_amt:
        print("Insufficient funds!")
    else:
        total_amt = total_amt - withdraw_amt
        print("Available balance:",total_amt)
    
def deposit(deposit_amt):
    global total_amt 
    total_amt = total_amt + deposit_amt
    print("New balance is:",total_amt)
    
def checkBalance():
    global total_amt 
    print("Available balance:",total_amt)
    

print("""Would you like to perform 
       1.Withdrawal
       2.Deposit
       3.Check Balance
       4.Exit\n""")
while(True):   
    choice = int(input("\nEnter you choice:"))
    if(choice == 1):
        withdraw_amt = int(input("Enter the amount to withdraw:"))
        withdraw(withdraw_amt)
    elif(choice == 2):
        deposit_amt = int(input("Enter the amount to deposit:"))
        deposit(deposit_amt)
    elif(choice == 3):
        checkBalance()
    elif(choice == 4):
        print("Exiting...")
        break
    else:
        print("Enter valid choice!")