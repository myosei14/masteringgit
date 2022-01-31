balance = 0
deposit = int(input("How much do you want to deposit?"))
print("You now have a balance of ", str(balance + deposit))
withdrawal = int(input("How much do you want to withdraw?"))
if withdrawal > deposit:
    print("Insufficient balance")
    print("Please, Check your balance")

else:
    print("Your current balance is", str(deposit - withdrawal))

