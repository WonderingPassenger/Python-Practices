#Here the methods of changing the case-types of the string using the in-built finctions are discussed
'''
1.Lower case : Converts the total string to lower case.
2.Upper case : Converts the total string to upper case.
3.Capitalize : Capitalizes the first letter of the string.
4.Title : Capitalizes the first letter of each word in the string.
5.Swap : Converts the lower to upper and upper to lower cases.
'''

lc = input("1. Lower case: \nEnter the string : ")
print(lc.lower())
uc = input("\n2. Upper case : \nEnter the string : ").upper()
print(uc)
c = input("\n3.  Capitalise : \nEnter the string : ").capitalize()
print(c)
t = input("\n4. Title : \nEnter the string : ").title()
print(t)
s = input("\n5. Swap : \nEnter the string : ")
print(s.swapcase())