bank_name = input("Enter the Bank name :")
bank_address = input("Enter the bank address :")
bank_IFSC = input("Enter the bank IFSC code :")
def account_details():
    print("BANK ADDRESS:",bank_address,"\nBANK IFSC :",bank_IFSC)
    account_balance = 500000.00
    account_deposit = float(input("Enter the depositing amount :"))
    account_balance = account_balance+account_deposit
    print("Available account balance =",account_balance)
    amount_withdrawal=float(input("Enter the withdrawal amount :"))
    account_balance = account_balance-amount_withdrawal
    print("Available account balance =",account_balance)
    GST=account_balance*(5/100)
    print("Intrest for the account balance is",GST)
    account_balance = account_balance+GST
    print("Available account balance =",account_balance)
account_details()
    

