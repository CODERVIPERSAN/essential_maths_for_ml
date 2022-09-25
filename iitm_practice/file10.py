from pickle import STOP
import numpy as np


arr=[]
com=input()
while com!='STOP':
    arr=arr+[com]
    com = input()
arr=arr+['STOP']
if(len(arr)>2):
    arr1=[arr.count('RIGHT')-arr.count('LEFT'),arr.count('UP')-arr.count("DOWN")]
else:
    arr1=[0,0]

print(abs(arr1[0])+abs(arr1[1]))

# #     com=input()
# while True:
#     if(com=="STOP"):
#         break
#     if(com=='START'):
#         arr=np.array([0,0])
#         com = input()
#     elif(com=='UP'):
#         arr+=np.array([0,1])
#         com = input()
#     elif(com=='RIGHT'):
#         arr+=np.array([1,0])
#         com = input()
#     elif(com=='DOWN'):
#         arr+=np.array([0,-1])
#         com = input()
#     elif(com=='LEFT'):
#         arr+=np.array([-1,0])
#         com = input()
# print((abs(arr[0])+abs(arr[1])))

