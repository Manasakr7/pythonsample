class bank:
    bname='ICICI'
    ROI=14
    MBL='MUMBAI'
    def __init__(self,a,b,c):
        self.name=a
        self.age=b
        self.bal=c
    def display(self):
        print('Name:',self.name)
        print('Age:',self.age)
        print('Balance:',self.bal)
        print('bname:',self.bname)
        print('ROI:',self.ROI)
        print('MBL:',self.MBL)
        print('-'*25)
    def deposit(self,amt):
        self.bal+=amt
        print('Deposit done successfully')
        print('-'*25)
    def withdraw(self,amt):
        if self.bal>=amt:
            self.bal-=amt
            print('Withdraw done successfully')
            print('-'*25)
        else:
            print('Insufficient balance',self.bal)
    @classmethod
    def chng_roi(cls,new_roi):
        cls.ROI=new_roi
        print('ROI has been modified')
        print('-'*25)
    @classmethod
    def disp_cls(cls):
        print('bname:',cls.bname)
        print('ROI:',cls.ROI)
        print('MBL:',cls.MBL)
        print('-' * 25)
dinga=bank('dinga',23,1000)
dingi=bank('dingi',21,3000)
dingi.display()
bank.display(dinga)
dinga.deposit(500)
dingi.withdraw(400)
bank.chng_roi(17)
dinga.chng_roi(19)
dingi.display()
dinga.display()
bank.disp_cls()




