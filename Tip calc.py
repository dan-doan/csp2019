yesList = ["yes", "ya", "duh", "ofc", "why not", "yes thank you"]

menu = [(1, "Food", 3),
      (2, "Water", 1),
      (3, "Dessert", 4),
      (4, "Airpods", 456),
      (5, "Minion", 1053),
      (6, "Canopy", 0.5)
]



print("Menu")

for each in menu:
  totalSpaces = 100
  pt1 = str(each[0]) + ". Item: "+ each[1]
  spacesLeft = totalSpaces - len(pt1)
  extraSpaces = spacesLeft - 70
  pt2 = ""
  for x in range(extraSpaces):
    pt2 = pt2 + " "
  pt3 = "Cost: $"+ str(each[2])
  print(pt1 + pt2 + pt3)






print('Place your order. For example to get Minion, Airpods and Food type (without quotes) "5,4,1"')
ch = input("")


if isinstance(ch, tuple):
    orderedNumbers = list(ch)
else:
    orderedNumbers = [ch]
    
    

orderedFoodItems = []
orderedFoodPrice = []
total = 0
for each in orderedNumbers:
    orderedFoodItems.append(menu[int(each-1)][1])
    orderedFoodPrice.append(menu[int(each-1)][2])
    total = total + menu[int(each-1)][2]
    
print("Total = $" + str(total))


tipQuestion = raw_input("Do you wanna tip the computer?")


if tipQuestion in yesList:
    tipPercent = raw_input("How much do you wanna tip?")
    if tipPercent[-1:]== '%':
        tipPercent = tipPercent[:-1]
    
    total = ((float(tipPercent)/100)*total) + total
    print("Your New total is $" + str(total))
    

split = raw_input("Do you wanna split the bill?")
if split in yesList:
    numberOfPeopleToSplit = float(raw_input("How many people are ordering abstract things from a computer?"))
    eachPersonPays = total/numberOfPeopleToSplit
    print("Each person pays $" + str(eachPersonPays))
    
print("Are you happy with your life?")
# I dont care what you answer