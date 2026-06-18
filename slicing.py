#Slicing : Selection of the specific characters of a string in a definite pattern

a= '''
Slicing is process of specific selection of the character(s) in the string.
'''

print(a[1:20:2])   #In range [Start:Stop:Increament/Decreament]
print(a[::])       #If we don't mention the values then it takes the default values([0:lastStringValue:1])
print(a[::-1])     #Reverse indexing