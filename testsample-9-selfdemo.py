class ProgStaff:
    companyName = 'Programming Lab'

    def __init__(self, pSalary):
        self.salary = pSalary

    def printInfo(self):
        print('Company name is ', ProgStaff.companyName)
        print('Salary is ', self.salary)


peter = ProgStaff(2500)
peter.printInfo()

ProgStaff.companyName = 'sdfdfdf'
peter.printInfo()

class Staff:
    def __init__(self, pPosition, pName, pPay):
        self.position = pPosition
        self.name = pName
        self.pay = pPay
        print('Creating Staff object')

    def __str__(self):
        return ("Position = %s, Name = %s, Pay = %d" %(self.position, self.name, self.pay))

    def calculatePay(self):
            prompt = "\nEnter number of hours worked for %s: " %(self.name)
            hours = input(prompt)
            prompt = "\nEnter hourly rate for %s: " %(self.name)
            rate = input(prompt)
            self.pay = int(hours)*int(rate)
            return self.pay

sam = Staff("Technician", "Sam", 2500)
print(sam)

# creating a subclass from parent class Staff
class ManagementStaff(Staff):
    def __init__(self, pName, pPay, pAllowance, pBonus):
        super().__init__('Manager', pName, pPay)
        self.allowance = pAllowance
        self.bonus = pBonus

    def calculatePay(self):
        basicpay = super().calculatePay()
        selfpay = basicpay + self.allowance
        return selfpay

    def calculatePerfBonus(self):
        prompt = "\nEnter grade for %s: " %(self.name)
        grade = input(prompt)
        if (grade == 'A'):
            self.bonus = 1000
        else:
            self.bonus = 0
        return self.bonus

    class BasicStaff(Staff):
        def __init__(self, pName, pPay):
            super().__init__('Basic', pName, pPay)

diego = ManagementStaff("Diego", 2500, 400, 600)
print(diego)