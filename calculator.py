s = input("Enter \"Compute\" to compute : ")

while(s== "Compute"):
    n1 = float(input("Enter a number : "))
    n2 = float(input("Enter a numner : "))
    o =input("Enter the operation(+,_,%,*,/) : ")
    if o == '+':
        a = n1+n2
    elif o == '-':
        if n1>=n2:
            a=n1-n2
        else :
            a=n2-n1
    elif o=='*':
        a = n1*n2
    elif o=='/':
        if n1>=n2:
            a=n1/n2
        else:
            a = n2/n1
    elif o=='%':
        if n1>=n2:
            a=n1%n2
        else:
            a=n2%n1
    else :
        print("Invalid operation!!")
    print("Your answer = ",a)
    b= input("Enter \"Exit\" to exit : ")
    if b=="Exit":
        s="No"