##My_variable = 5
##print(My_variable)

##variable_type = type(My_variable)
##print(type(My_variable))


### OPERATORS

# num = (3+4/5)**2
# print(num**(1/2))

# ###CLASS WORK
# a=3
# b=4
# c=9
# num = (b + b**2 - (4*a*c)**(1/2) / (2*a))
# print(num)

# t=12
# n=6
# r=0.08
# p=10000
# Answer = p*(r + (r/n))**(n*t) 
# print(Answer)

#*Creating a function*
# def print_lumba():
#     print("I'm Lumbajack, cooking a function code")
#     print("I know how weird it is, don't worry about a thing....lumbi ")
# print_lumba()

# def repeat():
#     #print_lumba()
#     print("lubma \n"*4)

# repeat()    

#loop (for and while)
#print natural numbers 1-10
# i = 0
# while i<=10:
#       print(i)
#       i+=1

#printing a number pattern
#setting number of rows to 5
#using range (start(0), stop(row+1), step(1))
# rows = 5
# for i in range(0, rows+1, 1):
#     #running inner loop (i+1 times)
#     for n in range(1, i+1):
#         print(n, end=  " ")
    
#     print("")


def count_down(n):

    while n > 0:
        print(n)
        n = n-1
        print("BoOm!")
count_down()        