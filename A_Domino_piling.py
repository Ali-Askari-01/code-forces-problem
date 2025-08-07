# M,N=map(int,input().split())
# count=0
# z=int(N/2)
# if (N%2!=0):
#   count+=1
# x=z*M
# count+=x
# print(int(count))
M,N=map(int,input().split())
prod=M*N
count=int(prod/2)
print(count)