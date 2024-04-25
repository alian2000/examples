# creating a class with the name Student
# __init__ to initialize only and not to set new values
# create a setter method to set new values

class student:
    def __init__(self, name , age):
        
        self.name= name  #object_variables or property = parameter
        self.age = age   #object_variables or property = parameter 
    def get_name(self):
        return self.name
        #You can use the return statement to make your functions send Python objects back 
        # to the caller code. These objects are known as the function’s return value. 
        # You can use them to perform further computation in your programs.
    
    def get_age(self):
        return self.age
        
    def get_student(self): 
        return self.name,self.age
        
        
    
    def set_student(self, name,age): 
        self.name = name
        self.age = age

student1 = student("usama",48) # create an object or instance of the class

# setting the age using setter 
student1.set_student("tamer", 15)
  

# retrieving age using getter
print(student1.get_name())
print("-----------------------------------")
print(student1.get_student())
print("************************************")


print(student1.name) 
print(student1.age) 

student1.set_student("wafa",41)
print("--------------------------------------")
print(student1.name)
print(student1.age) 


testInstance = student("usama",49)
print(testInstance.name)
print(testInstance.age) 