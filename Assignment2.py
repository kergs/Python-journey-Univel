#finding the number of students subbed to Eng and french newspaper
print("Enter the student's number row (separated with a 'SPACE').")
english_sub = set(input("ENGLISH:\n>>").split(" "))
french_sub = set(input("FRENCH:\n>>").split(" "))

#Finding the total number of student with atleast one subscription
e_f = english_sub.union(french_sub)
print(f"Hence {len(e_f)} students subscribed to at least one Newspaper.")



