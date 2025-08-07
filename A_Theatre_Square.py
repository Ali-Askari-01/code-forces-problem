n, m, a = map(int, input().split())
z=int(n/a)
count=z
if (n%a!=0):
  count+=1
x=int(m/a)

if (m%a!=0):
  x+=1
count=count*x
print(count)

# 1 2 3 4 5 6  a = 4 = > m/a 6 %4