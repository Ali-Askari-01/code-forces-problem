a=input()
distinct = set(char.lower() for char in a if char.isalpha())
count=len(distinct)

if(count%2==0):
  print("CHAT WITH HER!")
else:
  print("IGNORE HIM!")