n=int(input())
count=0
for val in range(1,n+1):
  a, b, c = map(int, input().split())
  if (a == 1 and b==1 and c==1):
    count+=1
  elif(a==0 and b==1 and c==1):
    count+=1
  elif(a==1 and b==0 and c==1):
    count+=1
  elif(a==1 and b==1 and c==0):
    count+=1
  else:
    count=count+0

print(count)

