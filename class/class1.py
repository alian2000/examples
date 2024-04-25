class location() :
    name="Usama"
    latitude = "25.594095"
    longtitude = "85.137566"
    city="CHICAGO"
    luckNumbers=[1,3,5,7,9]
    state="IL"
    country="USA"
    zipCode=60502
    age=100
    pic="pic1.png"
    price=1000
    
print(location.name)
customer1=location()
#print(location.__dict__)
print("*****************************************************")
print(customer1.luckNumbers)
print(customer1.luckNumbers[4])   # array variable in a class
customer1.luckNumbers[4]=19
customer1.name="nashwan"
print("new number= ",customer1.luckNumbers[4]) # update array variable in position 4 in a class

print (customer1.state)
print("discounted price= ",customer1.price*.80)

customer1.age=40
print(customer1.age)
print(customer1.age+5)

print (customer1.name.upper())
print (customer1.city.lower())
print (customer1.latitude,customer1.longtitude)
print("-------------------------")

customer2=location()
print (customer2.state)
print(customer2.age) #add a comment
print (customer2.price)
print (customer2.zipCode)


print("___________________________________________________________")
print(location.__dict__)