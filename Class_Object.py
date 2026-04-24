class Student:
# __init__ run automatically when object is created
    def __init__(self, name,marks):
        #  self.name it store data inside object
        self.name=name
        self.marks=marks
# it prints the value
    def display(self):
        return self.name,self.marks
        # print("My name is",self.name)
        # print("Total marks is",self.marks)
s1=Student("Akash",495)
print("My name is",s1.name)
print("Total marks is",s1.marks)

# ---------------------------------------------------------------------

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length * self.width

    def parameter(self):
        return 2 * (self.length + self.width)

r1=Rectangle(5,3)
print("Area of Rectangle:",r1.area())
print("Parameter of Rectangle:", r1.parameter())

# ----------------------------------------------------------------------
class BankAccount:

    def __init__(self,balance):
        self.balance = balance

    def deposit(self,amount):
        self.balance+=amount
        print("Deposeted",amount)

    def withdraw(self,amount):
        if amount<= self.balance:
            self.balance -=amount
            print("withdraw",amount)
        else:
            print("Insufficent balance")   

acc = BankAccount(1000)     
print(acc.balance)             
acc.deposit(500)
acc.withdraw(1500)
print("Final balance",acc.balance)

# 4

class Temperature:
    def __init__(self,celsius):
        self.celsius=celsius

    def to_fahrenheit(self):  
        return (self.celsius*9/5) + 32

temp=Temperature(25)
print("Fahrenheit",temp.to_fahrenheit())   

# 5

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0


c = Counter()
c.increment()
c.increment()
print("Count:", c.count)

c.reset()
print("After reset:", c.count)

# 6
class DatasetInfo:

    def __init__(self,name, row,columns):
        self.name=name
        self.row=row
        self.columns=columns

    def Display_summary(self):
        print("Name",self.name)
        print("Total rows",self.row)
        print("Total columns",self.columns)
info=DatasetInfo("Sales Data",500,10)
info.Display_summary()

# 7

class Product:

    def __init__(self,name,price):
        self.name=name
        self.price=price

    def discount(self):
            self.price = self.price*0.9

    def display(self):
        print("Name -",self.name)
        print("Price -",self.price)   

p1=Product("Laptop",10000)
p1.discount()
p1.display()             


# 8
class DataCleaner:

    def __init__(self,values):
        self.value=values
        print("---------------Data Cleaner-----------------")
        print("Values",self.value)

    def remove_null(self):
        self.value= [i for i in self.value if i is not None]
        print("Removing Null",self.value)

    def remove_duplicates(self):
        # self.value= list(set(self.value))
        # print("Removing Duplicates",self.value)

        seen = set()
        new_list = []
        for i in self.value:
            if i not in seen:
                seen.add(i)
                new_list.append(i)
        self.value=new_list
        print("Removing_duplicates -",self.value)            

    def display(self):
        print("Final result -",self.value)
        return(self.value)

value = [10, None, 20, 10, 30, None, 40]
data=DataCleaner(value)
data.remove_null()
data.remove_duplicates()
data.display()

# 9
class Statistics:
    def __init__(self,data):
        self.data=data

    def mean(self):
        return sum(self.data)/len(self.data)
    def maximum(self):
        return max(self.data)
    def minimum(self):
        return min(self.data)
    def count(self):
        return len(self.data)

nums = [10, 20, 30, 40, 50]  
s = Statistics(nums)

print(s.mean())
print(s.maximum())
print(s.minimum())
print(s.count())

# 10
class ColumnSelector:
    def __init__(self,data):
        self.data=data

    def select(self,key):
        return {k: self.data[k] for k in key if k in self.data}
    def drop(self,key):
        return {k:v  for k,v in self.data.items() if k not in key}    

record = {"name": "Akash", "age": 25, "salary": 50000, "city": "Delhi"}

cs = ColumnSelector(record)

print("Selected:", cs.select(["name", "salary"]))
print("Dropped:", cs.drop(["city"]))

# 11

class Dataset:
    def __init__(self,data):
        self.data=data

class SalesDataset(Dataset):
    def total_revenue(self):
        return sum(self.data)

sales = SalesDataset([100, 200, 300, 400])          
print("Total Revenue:",sales.total_revenue())

# 12

class EmployeeAnalyzer:
    def __init__(self, salaries):
        self.salaries = salaries

    def average_salary(self):
        return sum(self.salaries) / len(self.salaries)

    def highest_salary(self):
        return max(self.salaries)

    def total_employees(self):
        return len(self.salaries)


emp = EmployeeAnalyzer([30000, 45000, 50000, 60000])

print("Average:", emp.average_salary())
print("Highest:", emp.highest_salary())
print("Total employees:", emp.total_employees())

# 13
class SalesAnalyzer:
    def __init__(self,values):
        self.values = values

    def total_sale(self):
        return sum(self.values)
    def average_sale(self):
        return round(self.total_sale()/len(self.values))
    def highest_sale(self):
        total = self.total_sale()
        count= len(self.values)
        return total//count
        # return max(self.values)
    def lowest_sale(self):
        return min(self.values)
sales_data = [1200, 1500, 1800, 1100, 2000, 1700]
result = SalesAnalyzer(sales_data)
print(result.total_sale())
print(result.average_sale())
print(result.highest_sale())
print(result.lowest_sale())        

