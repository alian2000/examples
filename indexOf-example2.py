str1 = "usama.alian@gmail.com"
str2 = "@";
result= str1.index(str2, 0, len(str1))                      #look for str2 value and start from position 0 to the end 
print("The index where the substring is found:", result)
print(str1[result+1:len(str1)])                             #print the domain without the @ sign by adding one
print(str1[0:result])
