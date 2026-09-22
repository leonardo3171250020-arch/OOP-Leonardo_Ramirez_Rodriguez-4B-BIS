class BankAccount:
  def __init__(self, holder, balance):
    self.holder = holder
    self.__balance = balance
  
  def check_balance(self,):
    print(f"The balance is of: ${self.__balance}")

  def ProcessPayment(self,method):
    withdrawal=0
    print (f"Current account balance: {self.__balance}")
    match method.name:
        case "creditcard":
            print(f"The payment will be of $300")
            withdrawal=300
        case "paypal":
            print(f"The payment will be of $250")
            withdrawal=250
    if withdrawal>self.__balance:
      print("You cant withdrawal more money than the account's balance")
    else:
      self.__balance-=withdrawal
      print(f"Final account balance: {self.__balance}")
      return(self.__balance)

class PayMethod:
  def __init__(self,name):
    self.name=name

user1=BankAccount("carlos",3000)
paymethod1=PayMethod("paypal")
paymethod2=PayMethod("creditcard")

user1.ProcessPayment(paymethod1)
user1.ProcessPayment(paymethod2)
