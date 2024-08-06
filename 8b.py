file = open("file.txt", "w")
for i in range(5):
  text = input("Enter text: ")
  file.write(text + "\n")
file.close()

with open("file.txt", "r") as file:
  text = file.read()
  words = text.split()
  Upper = 0
  lower = 0 
  digits = 0
  for word in words:
      for char in word:
          if char.isupper():
              Upper+=1
          elif char.islower():
              lower+=1
          elif char.isdigit():
              digits+=1

  print("Number of uppercase letters: ", Upper)
  print("Number of lowercase letters: ", lower)
  print("Number of digits: ", digits)

