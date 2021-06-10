import random
secret_number=random.randint(1,10)
while True:
  guess = int(input("Guess a number: "))
  if guess == secret_number:
    print("Congrats!!.You won!")
    break
  else:
    print("Try again. :(")