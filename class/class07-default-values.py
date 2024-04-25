import logging
logging.basicConfig(filename='class07-default-values.log', level=logging.INFO,
                    format='%(levelname)s:%(message)s')

class Person:
    # name="name"
    # age=0
    def __init__(self, name, age):        #method to intialiaze class parameters
        self.name= name
        self.age = age
        logging.info('Created Employee: {} - {}'.format(self.name, self.age))

    def printDetails(self):              #method to print values07-de   
        print("\n Any Person Details")
        print("Name :", self.name)
        print("Age  :", self.age)
        logging.info('Print Employee info.: {} - {}'.format(self.name, self.age))
    
    def set_student(self,name,age): #methods to set new parameter values
        self.name = name
        self.age = age
        logging.info('Update Employee: {} - {}'.format(self.name, self.age))

person1 = Person("tamer",4)  # you need a setter method to set name/age values,this way you are creating an instance with default values
person1.printDetails()
x=6
logging.info('XXXXXXX: {}'.format(x))
print("------------------------------------------------------")

person1.name = "Mike"
person1.age = 21
person1.printDetails()

person1.set_student("Fayez Al-Dwairi",61)  #a setter method to set new values 
person1.printDetails()         #method to print out class
print("------------------------------------------------------")
print(person1.__dict__)  # print class details using builtin dict method

person2= Person("wiki",2)  # you need a setter method to set name/age values,this way you are creating an instance with default values
person1.printDetails()

person3= Person("Usama Alian",49)

