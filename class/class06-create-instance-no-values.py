# creating a class with the name Student
# __init__ to initialize only and not to set new values
# create a setter method to set new values
class Student:

   # constructor of the student class
   def __init__(self,studentName,rollNumber):

      # initiaizing the values of attributes with None
      self.studentName = "Dan"
      self.rollNumber = 18
      print('The Value of Student Name:',self.studentName)
      print('The Value of Roll Number:',self.rollNumber)

#Creating the Object for the student class

studentObject1=Student("usama","48")
studentObject2=Student("nour",19)
print(studentObject2.studentName)
studentObject3=Student("wix",4)
print(studentObject3.rollNumber)

studentObject4=Student("zayed",5)
print(studentObject4.studentName,studentObject4.rollNumber)

