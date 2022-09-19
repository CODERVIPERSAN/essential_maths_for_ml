start = input()
end = input()

row1 = ord(start[0])%65
col1 = int(start[1])-1

row2 = ord(end[0])%65
col2 = int(end[1])-1


flag =False
rowc = row1
colc = col1
while(rowc>=0 and colc>=0):
    if(rowc==row2 and colc==col2):
        # print(rowc,colc)
        flag =True
        
        break
    # print(rowc,colc)
    rowc-=1
    colc-=1

rowc = row1
colc = col1
while(rowc<8 and colc<8 and not flag):
    if(rowc==row2 and colc ==col2):
        # print(rowc,colc)
        flag = True
        break
    rowc+=1
    colc+=1

if(not flag):
    print("NO")
else:
    print("YES")