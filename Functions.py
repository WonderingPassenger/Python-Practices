# Functions are the set of codes that can be reused multiple times to perform a certain task.
'''
Syntax : 
    def functionName(parameter(s)):
        codes
    
    functionName(arguement(s));  #Here, bydefault the arguements get the order as relative to parameters respectively.
                        OR   We may also use it as:
    funtionName(parameter1=arguement1, parameter2=arguement2)
'''

def student(name,Class,studentID,Address):
    print(f"13. {name} with the student-ID : {studentID} , of class{Class} lives in {Address}.\n")

# Method 1 : Placing the arguements relative to the parameter of the function.
student('Shankar',6,56,"Ahmedabad")

# Method 2 : Directly appointing the values to the variables of the parameter.
student(Class=4,name="Sunistha",Address="Lucknow",studentID=74)

def fn(fn,mn,ln):
    n = fn+mn+ln
    print("23.",n)
    return n

nm = fn('Satya','Ranjan','Nayak')
print("27.",nm)


'''
Decorator : These are used to add extra lines of code to a certain code without changing the existing codes of the function.
    Syntax : def fun_name:
                "Some lines of codes"
                func()  #Here, the function executes.
            
            @fun_name   
            "Some lines of codes."
'''

def mainDecorator():
    print("Main Decorator.")

@mainDecorator
def Decor():
    print("Decorator")