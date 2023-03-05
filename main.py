def yes_no(question):
  while True:
    response = input(question).lower()

    if response == "yes" or response == "y":
      return "yes"
    elif response == "no" or response == "n":
      return "no"
    else:
      print("Please enter yes or no")
      

    



while True:
  want_instructions = input("Would you like the instructions? ").lower()

  if want_instructions == "yes":
    print("Instructions go here")
  elif want_instructions == "no":
    pass
    print("Ok we will proceed")
  else:
    print("Please enter yes / no")

print("we are done")
yes_no()