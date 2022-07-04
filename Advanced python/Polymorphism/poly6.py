#class - bank
#method 1 - account creation(name,accnt numb,min balance)
#method 2 - deposit(amount deposit,print total balance amount)
#method 3 - withdraw(amount withdraw,print total balance amount)

class Bank:
    bank_name="Federal"
    def accnt_creation(self,name,accnt):
        self.name=name
        self.accnt=accnt
        self.min_bal=3000
        self.tot_bal=self.min_bal
    def deposit(self,amt_deposit):
        self.amt_deposit=amt_deposit
        self.tot_bal=self.tot_bal+self.amt_deposit
        print("your",Bank.bank_name,"account has been credited",self.amt_deposit)
        print("your",Bank.bank_name,"total balance is",self.tot_bal)
    def withdraw(self,amt_withdraw):
        self.amt_withdraw=amt_withdraw
        if(self.amt_withdraw>self.tot_bal):
            print("insufficient balance")
        else:
            self.tot_bal=self.tot_bal-self.amt_withdraw
            print("your",Bank.bank_name,"account has been debited",self.amt_withdraw)
            print("your",Bank.bank_name,"total balance is",self.tot_bal)
ob=Bank()
ob.accnt_creation("tinu",12345)
ob.deposit(1500)
ob.withdraw(500)







