
value = input()

def makeodd(value):
    len_value = len(value)
    if(len_value%2==0):
        if(value[-1]=="."):
            return value[0:len_value-1]
        else:
            return value+"."
    else:
        return value 

value = makeodd(value)
start = ((len(value)-1)//2) -1
final = start +3
# print(start,final)
print(value[start:final])
print(makeodd(value))