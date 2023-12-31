#constructor
# it is special fuction to used for the memory allocation
#when the object is create constructor automatically called 1.default & 2.parameterized



class demo:
    def __init__(self,name,id): #default constructor
        self.empid =id
        self.empname=name
    def display (self):
        print ("employeename::",self.empname)
        print("employee is::",self.empid) 
d=demo("mina",1)
d.display()  
d1=demo("shubham",2)
d1.display()   
d2=demo("ram",3)
d2.display()


class book:
    def __init__(self,name,id,author,price):
        self.empid =id
        self.empname=name
        self.empauthor=author
        self.empprice=price
    def display (self):
        print ("employeename::",self.empname)
        print("employee id::",self.empid)
        print("employee author::",self.empauthor)
        print("employee price::",self.empprice) 
d=book("mina",1,"kirshna",23324)
d.display()  
d1=book("shubham",2,"trisha",12454)
d1.display()   
d2=book("ram",3,"tina",56789)
d2.display()

class car:
    def __init__(self,name,colour,model,price):
        self.empname=name
        self.empcolour=colour
        self.empmodel=model
        self.empprice=price
    def display(self):
        print("employee name::",self.empname)
        print("employee colour::",self.empcolour)
        print("employee model::",self.empmodel)
        print("employee price::",self.empprice)
b=car("thar","black",2023,2355477)
b.display()
b=car("scorpio","white",2020,12436567)
b.display()
b=car("baleno","blue",2022,354565687)
b.display()  
b=car("Innvocrysta","white",2021,3246678) 
b.display()
     
        





        


