#De="BooK"
#Ge="Worm"
#print(De+Ge)

#a= "Adebowale"
#print(a[3])

#name= "Harry Maguire"
#print(name[3:8])
#print(name[5])
#print(name[4:9:2])
#print(name[-1])

# name = input(">")
# macbook = 500000
# print(f"Dear {name}, you just purchsed 2 macbook pro at the price of #500,000 each.\nyour total cost is #1,000,000\n\n")

# print("This is a simple mathematical operation with python.\nRegards\n\tChisom") #breakline and tab

# print("It's for jacob")
# print('He said "We Dead"')# difference between "" and ''

# my_string = "this is a string"
# print(my_string.title())
# print(my_string.lower())
# print(my_string.upper())
# print(my_string.index("n"))
# print(my_string.rindex("n",0,15))
# print(my_string.find("n",0,10))
# print(my_string.isupper())
# print(my_string.istitle())
# print(my_string.isdigit())
 
 #Calculating Area
# print("Calculating the area of a Square:\n")
# length = int(input("Enter the length\n>"))
# print(f"The area of the square with length {length}cm is {length**2}cm")

#calculating interest
# p = int(input("initial capital:\n"))
# r = int(input("Rate (in pencetage)\n"))
# t = int(input("Time in years\n"))

# r/=100
# interest = p*r*t
# print(f"Interest ${p} at a rate of {r*100}% would give an interest of {interest} after {t} years")

# print("Please input you name\n")
# fn = input("First Name: \n")
# ln = input("Last Name: \n")
# username = (fn[0:3].upper()+ln[0:3])

# print(f"Hello {fn}, your username is {username}.")

###**String slicing..
# club = "Manchester"
# print(club[0:10])
# print(club[0:3])
# print(club[3:10])
# print(club[3:8])
# print(club[0:11:2])
# print(club[-1:-11:-1])
# print(club[-10:10])
# print(club[0:-1])

##Playing around with String (input)
# cele = input("Celebrity's Name: \n")
# celeAge = int(input("Date of Birth: \n"))
# Myage = int(input("When where you born?: \n"))
# Age_diff = Myage-celeAge
# print(f"{cele} is {Age_diff} years older than you")

#Calculating my time of jog
#started at 6:52 
# start_time=((6*60)+52)*60 #converting to secs
# easy_pace = ((8*60)+15)*2 #converting to secs and mulitipying by 2
# tempo_time = ((7*60)+12)*3 #converting to secs and mulitipying by 3
 
# food_time = (start_time + easy_pace + tempo_time) / 3600
# food_hour_int = int(food_time)
# food_min = (food_time - food_hour_int)*60

# print(f"Breakfast time is {food_hour_int}:{int(food_min)}am")

#Calling functions
# def add_number():
#     print(15-5)
# add_number()    



# import math  #import statment
# import math  #import statment
# print(math.factorial(5))
# print(math.factorial(5))
# print(type(5))
# print(type(5))


#Lambda Function
#Lambda Function
# a = lambda x : 4*x - 3
# a = lambda x : 4*x - 3
# b = lambda x : 3*x + 4
# b = lambda x : 3*x + 4
# b = lambda x : 3*x + 4
# c = a(b(-2))
# c = a(b(-2))


# print(c)
# print(c)
# from re import X


# pi = 3.142
# A = lambda r : pi* (r**2)

# print(A(4))

# t = 100100
# n = lambda x : t*10 + x**2
# print(n(3))

#global Variable
# def test_func(x,y):
#     print(x+y)
    

# test_func(15,10)

# def profile(name, age):
#     # age= 15
#     # name= "chisom"
#     print(name, age)


# profile("chisom", 15)

# employee_name1 = input("Enter Name:\n")
# employee_pay = int(input("Enter salary:\n")) 
# def profile(name, salary=9000):
#     print("Name:",name, "salary:",salary)  

# profile("James", 1000) 
# profile("Jane")   

# def print_twice(a,b):
#     print(a-b)
    
# print_twice(8,5) #positional argument
# print_twice(5,8)    #positional argument
# print_twice(b=8,a=5)
# print_twice(a=5,b=8)

# #defult argument
# def minus(a,b=3):
#     print(a-b)
# minus(8)  

# #split join replace
# a= ['A', 'quick', 'brown', 'fox', 'just', 'died.']
# b= " ".join(a)
# print(b.replace("brown", "white"))


#Map

# arr= [1,2,3,4,5]
# mapped = map(lambda y: y**2, arr)

# print(list(mapped))
# print(sum(arr))
# print(max(arr))
# print(min(arr))
# print(len(arr))

# def title():
#     a = "I am a Boy"
#     b = a.lower()
#     print(b.replace(" ", "-"))
# title()    
# #OR
# def title(word):
#     return word.replace(" ", "-").lower()

# print(title("How do you get killed"))

# def password(n,w):
#     a = n[:2]
#     b = w[-2:]
#     return a+b
# print(password("chisom","green"))


# a = lambda x : x + 15        
# print(a(30))    

# x=12
# y=2
# a= lambda x,y :x*y
#     #return a
# print(a(x,y))

#.numeric()
# five = lambda string : string.isnumeric()
# print(five("5"))

#.swapcase()
# tit = lambda string : string.swapcase()
# print(tit("I Am A boY"))

#get innput from the user
# name = input("filename\n ")
# #split and get the last element
# print(name.split(".")[-1])

# listy = [1,2,3,4,5]    
# listy1 = map(lambda x : x*3, listy)
# listy2 = map(lambda x : x**2, listy)
# print(list(listy1))
# print(list(listy2))

#list code
# a = [4,2,3,0,5,7,8,9]
# a[0] = 10
# print(a)
# print(a[0:])

# a = [1,2,3,4,5,6]
# b = [7,8,9,6,7,5]
# y = a+b
# y.sort()
# y.reverse()
# y.append(3)
# y.extend([94,40,39,48])
# y.insert(0,"kill")
# print(y)

#adding 52 and 24 in the list
# a = [2,3,4,2,[2,3,4,5,[4,52,2],5],24]
# b= a[4][4][1] + a[5]
# print(b)

#getting the second max and second min
# ty = [10,30,4,5,6,15,69]
# ty.sort()
# print(ty[1])
# print(ty[-2])
# print(ty[-3:])
# def largest(arr:list, n:int):
#     """This function returns the largest n value in the array: arr."""
#     arr.sort(reverse=True)
#     return arr[:n]
# print(largest([100,57,38,86,29,0], 2)) 

# def smallest(arr:list, n:int):
#     """this shows the smallest number in the list"""
#     arr.sort()
#     return arr[:n]
# print(smallest([100,57,38,86,29,0], 2))

#filter
# a = ["r","E","T","v","b","M"]
# cap = list(filter(lambda x : x.isupper(), a))
# print(cap)

# gee = input("Enter numbers> \n").split(",")
# g = map(int, gee)
# odd = list(filter(lambda x: x%2, g))
# print(odd)

# a = [1,3,4,5]
# b = [1,3,4,5]
# print(a==b)
# print(a is b)

# a = [4,7,9]
# b = a
# c = a.copy()
# print(b is a)
# print(c is a)

# a = [1,2,3,4,5,6]
# def middle(arr):
#     return arr[1:-1]
    
# print(middle(a))

# ada = [1,2,3,4,5,6,7,10,11]
# def m_number(ara):
#     ada.sort()
#     mid_point = len(ara)//2
#     return ara[mid_point]

# print(m_number(ada))

#If esle Statment
# a = "car"
# if a=="bike":
#    print("no result")
# elif a== "car":
#      print("it's a match")   
# else:
#      print("No match")  

# num = 15
# if num != 10:
#     print(num*2)
#     if num >= 10:
#        print("nice")
#        if num == 15:
#            print("wala") 
# else: 
#     print("no level")               

# print("Whats your exam score?")
# score = int(input(">>>\n"))

# if score <= 39:
#     print("F")
# elif score <= 49:
#     print("E")
# elif score <= 59:
#     print("D")
# elif score <= 69: 
#     print("C")
# elif score <= 79: 
#     print("B")
# elif score <= 100:
#     if score <=89: 
#        print("A-") 
#     elif score <=100:
#         print("A+")
# else:
#     print("OUT OF RANGE...")

#Random
import random
def game():
    a = [3,2,5,6,8,7]

    print(f"Select any number from {a}.\nWe hope it doesn't end in tears.")
    computer_choice = random.choice(a)
    random.shuffle(a)
    print("Guess the number:")
    user_choice = int(input(">>>"))
    if user_choice in a:
       if user_choice == computer_choice:
        print("All power belong to you comerade.")
       else:
           print("ahhh, Comerade biko try again.")
    else:
          print("Comerade, no be soo!.") 
while True:
    game()
    play_again = input("Keep Playing?\n").lower()
    if play_again =="yes":
        continue
    else:
        break
 
    
#Classwork
# import random
# text = """As you can see above, the get_sequence_upto function uses the yield keyword. The generator is called just like a normal function. However, its execution is paused on encountering the yield keyword. This sends the first value of the iterator stream to the calling environment. However, local variables and their states are saved internally\n"""
# print(text)

# subb_text = input("Enter text to search for:\n").lower()
# lowercase_text = text.lower()
# found = lowercase_text.find(subb_text)
# count =lowercase_text.count(subb_text)

# if found != -1:
#     print(f"{count} result(s) found!")
#     new_text = text.replace(subb_text, subb_text.upper())
#     print(new_text)
# else:
#     print(f"{count} result(s) found") 
# 
# Classwork Rock,Paper,scissors
# import random
# user_action = input("Please Enter your choice: (Rock, Paper or Scissor)\n").lower()
# actions = ["rock", "paper", "scissor"]
# com_action =  random.choice(actions)

# def rps_game():
     
#     if user_action == com_action:
#         print(f"both player selected {user_action}, It's a tie")
#     elif user_action == "rock":
#         if com_action == "scissor":
#             print("Rock breaks scissor, You Win!")
#         else:
#             print("you lose...")    
#     elif user_action == "scissor":
#         if com_action == "paper":
#             print("scissor cuts paper, You Win!")
#         else:
#             print("you lose!")
#     elif user_action == "paper":
#         if com_action == "rock":
#             print("Paper cover rock, you win")
#         else:
#             print("you lose..")
#     else:
#         print("Please Enter a Correct input.")     
# while True:
#       rps_game() 
      
#       play_again = input("Keep Playing?\n").lower()
#       if play_again =="yes":
#         continue
#       else:
#         break
           

#loop
# h = 10
# while h>0:
#     print(h)
#     h-=1
#     if h==0:
#         print("BoomChacaLacA!")
    

# n = 1
# while n<=10:
#     if n==10:
#         print("BoomChacaLacA!")  
#     else:
#         print(n)
#     n= n+1  
    
# i = 1
# while True:
#     print(f"Keep Playing{i}")
#     c = input("continue?\n")
#     if c== "yes":
#         i+=1
#         continue
#     else:
#         break    