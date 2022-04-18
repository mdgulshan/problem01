

class Account:
    def __init__(self, balance=0.0, name=''):
        self.balance = balance
        self.name = name
        self.nominee = None
    def Deposit(self, balance=0.0):
        self.balance = self.balance + balance
        print("Deposite is succesfull and the balance in account is %f" % self.balance)

    def Withdrawal(self, balance=0.0):
        if (self.balance >= balance):

            self.balance = self.balance - balance
            print("The withdraw is successfull and balance is %f" % self.balance)

        else:
            print("Insufficient balance")

    def AddNominee(self, name=''):
        self.nominee = name
        print(self.nominee)

from BankPackage import BankInfo as BNK


acct1 = BNK.Account(5000, "Sachin")
acct1.Deposit(1000)
acct1.Withdrawal(2000)
print(acct1)


acct2 = BNK.Account(3000, "Ali")
acct2.Deposit(500)
acct2.Withdrawal(250)
print(acct2)

if(acct1 == acct2):
    print("Thay have equal balance")
else:
    print("Thay have different balance")


if(acct1 != acct2):
    print("Oops!!! they are not equal")
else:
    print("wow!!!  they are equal")


if(acct2 > acct1):
    print("acct2 should pay more tax")
else:
    print("acct1 should pay normal tax")

if(acct2 < acct1):
    print("Sponsor for two children")
else:
    print("Start an Orphanage")

if(acct2 >= acct1):
    print("Go On Europe Trip")
else:
    print("Go for an excursion")


if(acct2 <= acct1):
    print("We can have coffee")
else:
    print("We can have meals")


acct1.AddNominee("Ranjini")
acct1.AddNominee("Ragini")
acct1.AddNominee("Malini")
acct1.AddNominee("Rukmini")


print(len(acct1))  # number of nominees


for nom in acct1:  # should iterate nominees
    print(nom)