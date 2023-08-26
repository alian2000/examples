# Python program to demonstrate
# while loop with True

N = 10
Sum = 0
print (N)

# This loop will run forever
while True:
     Sum += N
     N -= 1
     print(N)
     if N == 0:
         break

		
print(f"Sum of First 10 Numbers is {Sum}")
print ("this is the end")
