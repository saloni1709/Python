# find the total pofit/loss of each trader working in a trading firm. Info. regarding no of transaction  is unknown
empId = int(input("Enter Id: "))
if(empId != '-1'):
    trade = int(input("Enter trade Amount: "))
    pro_loss = 0
elif(trade != 0):
    pro_loss = pro_loss + trade
    trade = int(input("Enter Trade: "))
print(f"profit/loss for emp {empId} is {pro_loss}")
emp_id = input("\n ENter empId")
