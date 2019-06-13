number=int(input("Enter number of elements in array \n"))
addList=[i+1 for i in range(0,number)]
queries=int(input("Enter number of queries \n"))
for i in range(0,queries):
    left,right,val=map(int,input().split())
    for j in range(left-1,right):
        addList[j]=addList[j]+val
print(str(max(addList)))
        
