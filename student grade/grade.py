#the user inputs intiger value (the no of list indicies)    
# the user inputs his/her grades in a list
# calculate average of grades and the degree  
valid=False
while not valid:# true so the loop continue except for false
    try:
        no=int(input("Enter no of your grades:"))
        list=[]
        for i in range(no):
            x=float(input("Input your grades:"))
            list.append(x)
        if no<=0 or x<=0.0 :
            print("Invalid, Enter a countable +ve no. ")
        else:valid=True
    except ValueError:
         print("Invalid,Enter a numerical value.")
print("_________________________________________________________________")
av=sum(list)/len(list)
round(av,2)
print(f"Degrees:{list}")
print("Average degree:",av)
print("________________________________________________________________")
if av>=3.5 and av<=4:
 print("Congrats! Your grade is [Excellent^_^] (A)")
elif av<=3.5 and av>=3:
 print("Congrats! Your grade is [Very good] (B)")
elif av<=3 and av>=2.5:
 print("Congrats! Your grade is [Good] (C)")
elif av<=2.5 and av>=2:
 print("Congrats! Your grade is [Pass] (D)")
else:
 print("Unfortunately!Your garde is [Fail](F)")
print("________________________________________________________________")   
print("***********************{ THANK YOU }****************************")
print("________________________________________________________________")       