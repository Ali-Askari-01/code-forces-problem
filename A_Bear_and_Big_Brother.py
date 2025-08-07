a,b=map(int,input().split())
limak=a
bob=b
count=0
while bob>=limak:
  count+=1
  bob*=2
  limak*=3

print(count)
