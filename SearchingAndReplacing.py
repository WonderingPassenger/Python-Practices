#Here we shall be discussing how to search and replace a character in string with their indexed value(s).and
a = "Texts to test the the the the searching and replacing functions."

print("Searching : \nthe : ", a.find("the"))   #Searching gives the index value of the word's first letter .
# b=a.replace(a[32:41],"searching")
b=a.replace(a[14:16],"v")
print(b)
# print("\n",a,"\nReplacing : \n",b)

'''
Replacing replaces the selected character(s) , even if they are present later on in the text, and replaces them to the selected character(s) that we have texted.
'''