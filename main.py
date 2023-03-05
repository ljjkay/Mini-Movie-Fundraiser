def yes_no(question):
  while True:
    response = input(question).lower()

    if response == "yes" or response == "y":
      return "yes"
    elif response == "no" or response == "n":
      return "no"
    else:
      print("Please enter yes or no")


MAX_TICKETS  = 3
tickets_sold = 0

want_instructions = yes_no("Do you want the instructions? ")
if want_instructions == "yes":
  print("Instruction go here")

print()

while tickets_sold < MAX_TICKETS:
  name = input("Please enter your name or 'xxx' to quit ")
  if name == 'xxx':
    break

  tickets_sold += 1

  if tickets_sold ==MAX_TICKETS:
    print("Congraulation you have sold all the tickets")
  else:
    print("you have sold {} ticket/s. There is {} ticket/s left".format(tickets_sold, MAX_TICKETS - tickets_sold))
