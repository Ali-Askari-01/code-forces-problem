# t=int(input())
# for val in range(1,t+1):
#   n=int(input())
#   values = list(map(int, input().split()))
#   my_set = set(values)
#   score=0
#   i=0
#   while i in my_set:
#     i+=1
#   score+=i
#   total=sum(my_set)
#   score=score+total
#   print(score)

t=int(input())
for _ in range(1,t+1):
  n=int(input())
  values=list(map(int,input().split()))
  my_set=set(values)
  score=0
  score=sum(my_set)
  i=0
  while i in my_set:
    i+=1
  score+=i
  print(score)
