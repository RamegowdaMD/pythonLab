file = open("file.txt", "w")
for i in range(5):
  text = input("Enter text: ")
  file.write(text + "\n")
file.close()

with open("file.txt", "r") as file:
  text = file.read()
  words = text.split()
  longest = max(words, key=len)
  shortest = min(words, key=len)
  print("Longest word: ", longest ," with length " , len(longest))
  print("Shortest word: ", shortest ," with length " , len(shortest))