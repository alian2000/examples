class location :
    def __init__(self, fname,age):
        self.fname=fname
        self.age=999
        
    def first(self,age):
        self.age=age
        return self.age - 8
    def capital(self,fname):
        self.fname=fname
        return self.fname.upper()
    
    
        
      
mycity=location ("usama",18)
print("mycity= ",mycity.fname,mycity.age)
mycity1=location ("ahmed",49)
print("mycity1= ",mycity1.fname,mycity1.age)
print("-----------------------------------------------------------")
print(mycity1.first(49))
print(mycity1.first(49)-41)
print("-----------------------------------------------------------")
print(mycity1.capital("wasim"))
print(mycity1.fname.upper())
