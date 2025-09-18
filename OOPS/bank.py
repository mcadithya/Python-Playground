class Bank:

    def __init__(self,acc_holder,acc_num, account_type ,balance,mpin ):

        # self.acc_holder,self.acc_num, self.account_type , self.balance,self.mpin = arg

        self.acc_holder = acc_holder

        self.acc_num = acc_num

        self. account_type = account_type

        self.__balance = balance

        self.__mpin = int(mpin)

    def deposit(self,mpin,amount):

        if self.__mpin == mpin:
           
            if amount >0:

                self.__balance += amount

                print(f"Dear {self.acc_holder} , your account number {self.acc_num} hasbeen creadited with amount {amount}. Your balance is : {self.__balance}")
            
            else:

                print("Account must be greater than zero")
        
        else:

            print("incorrect mpin")

    def Withdraw(self, amount, mpin): 

        # if amount >0 : 

        if self.__mpin == mpin:

            if self.__balance>=amount :

                self.__balance-=amount

                print(f"Dear {self.acc_holder} , your account number {self.acc_num} hasbeen debited with amount {amount}. Your balance is : {self.__balance}")
                
            else:

                print("Account balace is not enough for withdrawal")

        else:

            print("incorrect mpin")
    
    def update_mpin(self,acc_holder,acc_num,new_mpin):

        if acc_holder==self.acc_holder and acc_num==self.acc_num:

            self.__mpin=new_mpin

            print(f'dear {self.acc_holder},your account number{self.acc_num} has updated mpin successfully')

    def __str__(self) :    #gives the string representation of object

        return{f'{self.acc_holder}-{self.acc_num}'}  
    
    def display(self):

        print(self.acc_holder,self.acc_num,self.acc_type,self.balance,self.__mpin)



bank_object = Bank("adithya", 147896586,"credit",478)

bank_object.deposit(478,2000)

bank_object.Withdraw(1000,478)

# bank_object.balance = 10000

print(bank_object.__balance)

print(bank_object.balance)




