n1=1 
while n1 == 1: 
    print("\n this is menu driven program")
    print(" 1) Addition \n 2) Multiplication \n 3) Division \n 4) Subtraction \n 5) FloorDivision\n 6)Raise to power ")
    num=int(input("Enter your choice"))
    if num==1:
        x=float(input("Enter the first number"))
        y=float(input("Enter the second number"))
        add=x+y
        print("the addition of ",x,",",y," =",add)
    elif num==2:
        x=float(input("Enter the first number"))
        y=float(input("Enter the second number"))
        mul=x*y
        print("The Multiplication of ",x,"",y," =",mul)
    elif num==3:
        x=float(input("Enter the first number"))
        y=float(input("Enter the second number"))
        div=x/y


        print("the division of",x,",",y,"= ",div)
    elif num==4:
        x=float(input("Enter the first number"))
        y=float(input("Enter the second number"))
        sub=x-y
        print("the subtraction of ",x,",",y,"=",sub)
    elif num==5:
         x=int(input("Enter the first number"))
         y=int(input("Enter the second number"))
         print("the floordivision is",x//y)
    elif num==6:
         x=float(input("Enter the first number"))
         y=float(input("Enter the second number"))
         sqr=x**y
         print("the value of",x,"raise to",y,"  is",sqr)
         print()
    else:
        print("Invalid choice")
    n=input("If u want to continue further click 1\n else click any key to exit!!") 
if n!="1": 
        exit()
n1=int(n)
#this is menu driven program
 #1) Addition       
 #2) Multiplication 
 #3) Division       
 #4) Subtraction    
 #6)Raise to power  
#Enter your choice2 
#Enter the first number8
#Enter the second number9
#The Multiplication of  8.0  9.0  = 72.0
#If u want to continue further click 1  
 #else click any key to exit!!
 # this is menu driven program
 #1) Addition 
 #2) Multiplication 
 #3) Division 
 #4) Subtraction 
 ##6)Raise to power 
#Enter your choice6
#Enter the first number5
#Enter the second number6
#the value of 5.0 raise to 6.0   is 15625.0

#If u want to continue further click 1     
# else click any key to exit!!
#this is menu driven program
# 1) Addition 
# 2) Multiplication 
# 3) Division 
 #4) Subtraction 
 #5) FloorDivision
# 6)Raise to power 
#Enter your choice5
#Enter the first number50
#Enter the second number5
#the floordivision is 10
#If u want to continue further click 1
# else click any key to exit!! 



