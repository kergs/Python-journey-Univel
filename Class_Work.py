#Converting Miles to Km
# def miles_km(miles,kilometers):
#     miles = float(input("Please Enter mile:\n"))
#     kilometers = miles * 1.6
#     print(kilometers, "kilometers")
# miles_km(1,1.6)    

# #Converting dollar to Naira
# def dn(dollar,naira):
#     dollar = int(input("Please enter dollar:\n"))
#     naira =  dollar*404
#     print("#",naira)

# dn(1,404) 

#Classwork *finding the averge and range
# a = [1,2,3,4,5]
# averga = sum(a)/len(a)
# print(averga)

# range = max(a)-min(a)
# print(range)

# a = input("please enter numbers:\n").split(",")

# a = (map(int, a))

# print(list(a))

# from math import sqrt
# import statistics
# st_Sc = input("Please Enter Students Score: \n").split(",") 
# sc = list(map(int, st_Sc))
# average = sum(sc)/len(sc)
# range = max(sc) - min(sc)
# s_d = map(lambda x: (x-average)**2, sc)
# sq_sd = sqrt(sum(s_d)/len(s_d))
# vari = sq_sd**2
# print("average: ", average)
# print("range: ", range)
# print("Standrad Deviation: ", s_d)
# print("variant", vari)

# averge = statistics.averger()



# #Age reminder
# age= int(input("Please Enter you year of birth:\n"))

# print(f"you were born in {2022-age}")

# def add_num(a,b):
#     print(a+b)
#     #return(a+b)
    

# x=add_num(4,6)
# print(x)

def factorial(n):
    if n==1:
      return 1

    return n * factorial(n-1)  

print(factorial(5)) 


#fruitful function example  
