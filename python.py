1=int(input("Enter the marks 1:"))
n2=int(input("Enter the marks 2:"))
n3=int(input("Enter the marks 3:"))
if((n1<=n2)and(n1<=n3)):
    avg=(n2+n3)/2
elif((n2<=n1)and(n2<=n3)):
    avg=(n1+n3)/2
else:
    avg=(n1+n2)/2
print("Average of best 2 test marks: ",avg)
