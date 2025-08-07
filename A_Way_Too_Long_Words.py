n=int(input())
for val in range(1,n+1):
  z=str(input())
  if (len(z)>10):
    print(z[0],end="")
    print(len(z)-2,end="")
    print(z[-1])
  else:
    print(z)