Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

#Question 1
print("Q1) Do you like Dawn or Dust?")

print(" 1) Dawn")
print(" 2) Dusk")
  
answer = int(input('Enter answer (1-2): '))

if answer == 1:
  Gryffindor += 1
  Ravenclaw += 1
elif answer == 2:
  Hufflepuff += 1
  Slytherin += 1
else:
  print("Wrong input.")

#Question 2
print("\nQ2) When I'm dead, I want people to remenber me as: ")
  
print(" 1) The Good")
print(" 2) The Great")
print(" 3) The Wise")
print(" 4) The Bold")    
  
answer = int(input('Enter answer (1-4):'))

if answer == 1:
  Hufflepuff += 2
elif answer == 2:
  Slytherin += 2
elif answer == 3:
  Ravenclaw += 2
elif answer == 4:
  Gryffindor += 2
else:
  print("Wrong input.")

#Question 3
print("\nQ3) Which kind of instrument most pleases your ear?")

print(" 1) The violin")
print(" 2) The trumpet")
print(" 3) The piano")
print(" 4) The drum")

answer = int(input('Enter answer (1-4): '))

if answer == 1:
  Slytherin += 4
elif answer == 2:
  Hufflepuff += 4
elif answer == 3:
  Ravenclaw += 4
elif answer == 4:
  Gryffindor += 4
else:
  print("Wrong input")

#Results
print("Gryffindor: ", Gryffindor)
print("Ravenclaw: ", Ravenclaw)
print("Hufflepuff: ", Hufflepuff)
print("Slytherin: ", Slytherin)

most_points = max(Gryffindor, Ravenclaw, Hufflepuff, Slytherin)

if Gryffindor == most_points:
  print("Gryffindor!")
elif Ravenclaw == most_points:
  print("Ravenclaw!")
elif Hufflepuff == most_points:
  print("Hufflepuff!")
else:
  print("Slytherin!")
