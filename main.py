MAX_TICKETS  = 3

tickets_sold = 0
while tickets_sold < MAX_TICKETS:
  name = input("Please enter your name or 'xxx' to quit ")
  if name == 'xxx':
    break

  tickets_sold += 1

  if tickets_sold == MAX_TICKETS:
    print("Congragulation you have sold all the tickets")
  else:
    print("you have sold {} ticket/s. There is {} ticket/s left")
