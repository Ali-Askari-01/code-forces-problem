n=int(input())
X=0
for val in range(1,n+1):
  z=str(input())
  if(z=="++X"):
    X+=1
  elif(z=="X++"):
    X+=1
  elif(z=="--X"):
    X-=1
  elif(z=="X--"):
    X-=1

print(X)