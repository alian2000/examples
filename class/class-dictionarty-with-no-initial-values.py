# you need to create an instance/object of the class
# you need to use class.method to set
# you need to use class.method to get 
# you need 
STUDENTS = {
  '1': {'name': 'Mark', 'age': 23, 'spec': 'math'},
  '2': {'name': 'Jane', 'age': 20, 'spec': 'biology'},
  '3': {'name': 'Peter', 'age': 21, 'spec': 'history'},
  '4': {'name': 'Kate', 'age': 22, 'spec': 'science'},
}
class studentlist:
    
    def __init__(self, id , name , age , spec ):
        self.id = 1
        self.name = "usama"
        self.age = 2
        self.spec= "devops"
        
    
    def create_dictionary():
        return STUDENTS
    
    def set_student(self,id,name,age, spec): 
        self.id = id
        self.name = name
        self.age= age
        self.spec = spec
    def get_student(self): 
        return self.id,self.name,self.age,self.spec
# student1 = studentlist.create_dictionary()
# print(student1)
student2 = studentlist( 2,"usa",2,"klm")
print(student2.name)
student2.set_student( 77,"Zico",23,"soccer")
print(student2.get_student())
print("_________________________________________")
print(studentlist.create_dictionary())