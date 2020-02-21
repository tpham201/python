a=input("Give me string:")
b=len(a)
c=-b
count=-1
d=""
while(count>=c):
    d=d+a[count]
    count=count-1
print(d)
if(a==d):
    print("string is palindrome ")
else: print("string is not palindrome ")
