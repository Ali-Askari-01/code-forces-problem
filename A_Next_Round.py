n,k=map(int,input().split())
count=0
lst=list(map(int, input().split()))
i=0
for val in lst:
  if(lst[i]>=lst[k-1] and lst[i]!=0):
    count+=1
    i+=1
print(count)
