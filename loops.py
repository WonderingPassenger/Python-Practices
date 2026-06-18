print("Here , the loops are discussed.\n1.if-else\n2.elif - ladder\n3.for - loop\n4.while - loop")
#_____________________________________________________

# 1. if - else
print("\n\n\n1. if - else")
i=float(input("Enter a natural number : "))
if i%2==0:
    print(i," is an even number.")
else :
    print(i," is an odd number.")

#-----------------------------------------------------

# 2. elif - ladder
print("\n\n\n2. elif - ladder")
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

#-----------------------------------------------
#for - loop
print("\n\n\n3. for - loop")
for i in range(1,5,2):
    for j in range(0,5,2):
        print(i,j)
    print("\n")


#-----------------------------------------------
#while - loop
print("\n\n\n4. while - loop")

i=1
while i<=20:
    print(i)
    i+=i