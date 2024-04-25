import time
import logging
from target import *

targets = {}   # target is dictionary where if you use [] it will be a list

try:
    # rotate from 0 to 180
    for angle in range(0, 180,1):
        distance=angle/2 + 2.1
        targets[angle] = Target(angle, distance)
        #print (targets)
        #print (angle,targets[angle])                   #prints the class objects and not the 
        #print (targets[angle].get_target())
except KeyboardInterrupt:
    print ("Radar Exit")
targets[4]
print (targets[4].get_target())
print(len(targets))
print("wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
print (targets)   #print the whole dictionary
print("wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
x = targets.get(10)
print("x= ",x)
x = targets.values()

print(x) #before the change

x = targets.values()
print("------------------------------------------------------------------------------")
for angel in targets:
  print(angel)
  print(targets[angel])
print("------------------------------------------------------------------------------")
