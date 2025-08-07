n=int(input())
s=input()
count=0
for val in range(len(s)-1):
  if (s[val]==s[val+1]):
    count+=1

print(count)
