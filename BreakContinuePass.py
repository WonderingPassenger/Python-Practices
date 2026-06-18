#Here we have discussed about BRREAK and CONTINUE syntax

#break
print("break : ")
for i in range(1,10):
    if i==6:
        break    #"break" is the command that helps the code to come out of the loop
    print(i)


#continue
print("\ncontinue : ")
for i in range(1,10):
    if i==6:
        continue    #"continue" is the command that helps the code to skip the current loop
    print(i)

#pass
print("\npass : ")
for i in range(1,10):
    if i==6:
        pass      #"pass" is the command that provides the coder to add logic later on , without disturbing the current execution of program.
    print(i)


'''
break : Totaly out of the loop
continue : Skips the current line of the loop
pass : No current impact. But, faciliates the coder for adding a new logic later-on.
'''