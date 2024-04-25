class location :
    def __init__(self, fname, lname,latitude,longtitude,city,state,country,zipcode=0,age=0):
        self.fname=fname
        self.lname=lname
        self.latitude = latitude
        self.longtitude = longtitude
        self.city=city
        self.state=state
        self.country=country
        self.zipCode=zipcode
        self.age=age
        
    def first(self,fname,age):
        self.fname=fname
        self.age=age
        return fname,age
    def newAge(self,age):
        self.age=age-10
        print(self.age)
        print(age)
        return age
    def smartAge(self):
        new_age=self.age-10
        print(new_age)
              
      
mycity=location ("usama","alian",33,34,"chicago","IL","USA",60525,21)
mycity1=location ("ahmed","khaleel",33,34,"Orland Park","IL","USA",60525,100)
print("mycity1= ",mycity1.city)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(mycity1.first("Ali",50))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
average=(mycity.age+mycity1.age)/2
print(average)
print(mycity.age+9)
print(mycity.city.upper())
print(mycity.city.upper().split("A")[0])

#print (mycity.__dict__)


print("reversed= ",mycity.city[::-1])
    
#mycity1.fisrt1("sama")
mycity1.newAge(73)
print(mycity1.__dict__)

mycity1.smartAge()