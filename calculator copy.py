#CALCULATOR 

def Substraction(n1,n2) :
    if n1 < n2:
        n = n2-n1
        f"{n2} - {n1} = {n}"
    else:
        n = n1 -n2
        f"{n1} - {n2} = {n}"

def Division(n1,n2) :
    if n2 == 0:
        "The value for denominator can not be '0'. Enter a different value."
    else :
        n = n1/n2
        f"{n1} / {n2} = {n}"        

Operation=input("Enter the operation to perform (1.Addition,2.Substraction,3.Multiplication,4.Division): ")
n1= input("Enter the first number : ")
n2= input("Enter the second number : ")

if Operation == '1' :
    n= n1+n2
    print(f"{n1} + {n2} = {n}")
elif Operation == '3' :
    n = n1*n2
    print(f"{n1} * {n2} = {n}" )
elif Operation == '4':
    print(Division(n1,n2))
elif Operation == '2'  :
    print(Substraction(n1,n2))
else :
    print("Invalid operation !")

