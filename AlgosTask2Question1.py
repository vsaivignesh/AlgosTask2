cases=int(input("Enter cases \n"))
validList=[]
for i in range(cases):
    valid=0
    line=str(input())
    largerThan=0
    for j in range(0,len(line)):
        if(line[j]=='<'):
            largerThan=largerThan+1
        else:
            largerThan=largerThan-1
        if(largerThan<0):
            break
        elif(largerThan==0):
            valid=j+1
    validList.append(valid)
for k in range(0,len(validList)):
    print(str(validList[k])+" \n")

        
        
