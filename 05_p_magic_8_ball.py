## importing the 'random' module
import random
## picking random numbers from 1 to 11
random_number = random.randint(1, 11)
#print(random_number)

name = ""
question = "Is Earth flat?"
answer = ""

if (name == ""):
  name = "A stranger"

if (random_number == 1):
  answer = "Yes - definitely"
elif (random_number ==2):
  answer = "It is decidedly so"
elif (random_number ==3):
  answer = "Without a doubt"
elif (random_number ==4):
  answer = "Reply hazy, try again"
elif (random_number ==5):
  answer = "Ask again later"
elif (random_number ==6):
  answer = "Better not tell you now"
elif (random_number ==7):
  answer = "My sources say no"
elif (random_number ==8):
  answer = "Outlook not so good"
elif (random_number ==9):
  answer = "Very doubtful"
elif (random_number ==10):
  answer = "Are you serious ?"
elif (random_number ==11):
  answer = "Come on, please..."
else :
  answer = "Error"

if (question == ""):
  print("Please ask a question")
else:
  print(name + " asks: " + question)
  print("answer: " + answer)