import random
secret_number=random.randint(1,10)
while True:
  guess = int(input("Guess a number between 1 and 10: "))
  if guess == secret_number:
    print("Congrats!!.You won!")
    break
  elif guess < secret_number:
    print("Guess again. Too low.")
   elif guess > secret_number : 
    print("Guess again. Too high")  
