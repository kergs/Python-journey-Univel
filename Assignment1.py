#Fermat’s theorem
#Creating a function that checks Fermat's Theorem
def check_fermat(a,b,c,n):
    if n>2 and (a**n)+(b**n)==(c**n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work...")   

#Collecting user input to check violation of Fermat's theorem
def user_input():
   # print("Please enter positive Intigers and the value for 'n' must be greater than 2...")
    a = int(input("Enter your value for 'a': "))
    b = int(input("Enter your value for 'b': "))
    c = int(input("Enter your value for 'c': "))
    n = int(input("Enter your value for 'n': ")) 
    check_fermat(a,b,c,n)
user_input()        