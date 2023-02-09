class bankaccount():
  def __init__(self, owner = '', balance = 0):
    self.owner = owner
    self.balance = balance 

  def __str__(self):
        print (f'Account owner: {self.owner}\n Account balance: ${self.balance}')
        
  def deposit(self,dep):
        self.balance += dep
        print('Deposit Accepted')
        
  def withdraw(self,wd):
        if self.balance >= wd:
            self.balance -= wd
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')


p1 = bankaccount("Arai" , 1000000)

      
p1.deposit(50)

p1.withdraw(75)

p1.withdraw(10000000)  