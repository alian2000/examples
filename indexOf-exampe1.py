str1 = "Hello!@Welcome to Tutorialspoint. Nour and Walid"

str2 = "Welcome"
print ("looking for =",str2)

print ("lenght of Array =",len(str1))

result= str1.index(str2, 5, 48) #look for space between location 1 and 15
print(result)
print ("======================================================================================")

result_final=str1.index(str2, 0, len(str1))               #using the buildin functions
print("The index where the substring is found:", result)
print("The index where the substring is found:", result_final)

print (str1.upper())
print (str1.lower())

x=("hello")
print (x)
#Reverse the text using [::-1]
print (x[::-1])
