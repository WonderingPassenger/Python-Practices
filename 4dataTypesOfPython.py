#There are several data types in python(integer, string, float,set, range , etc.). But, there are 4 main data-types .So ,the concepts of RANGE ,LIST, TUPLE and SETS-FROZEN SETS  are discussed below.

'''
1. Range : It's used to design loops .
    1. Syntax : range(start,stop,step of progression)
                By default start = 0 & Step of progression = 1
'''
# Range is used only for integeral - items.
a = range(1,16,2)
b = range(1,10)
c = range(6)
print("\nRange:")
for i in a:
    print(i)
print("\n")
for j in b :
    print(j)
print("\n")
for k in c:
    print(k)


'''2. List
'''

'''3. Tuple : These are used to store multiple items in a sequence ,with indexing.
        1. Syntax:  a=("item1","item2")
        2. Immutable(Unchangable)  : The values of the items cann't be changed or manipulated(add,change or remove).
        3. Inorder to make changes in tuple ,we have to change it to list-type first.
'''
tuple1 = ('string',"43",43,True,False,45.54,4+4j)
print("\nTuple : ")
print(tuple1)
tuple2 = list(tuple1)
tuple2.insert(1,"interprete")
print(tuple2)

#4. Sets and Frozen-sets 
