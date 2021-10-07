path = "products.txt"

def load_path(path):
  file = open(path, 'r')
  list = file.readlines()
  for i in range(len(list)):
    # clean up the lines in place
    list[i] = list[i].strip().split(',')
  return list

def search(str):
  found = []
  for item in inventory:
    for entry in item:
      if str in entry:
        found.append(display_product(item[1], item[2], item[3]))
  if len(found) < 1:
    return print("Item not found.")
  else:
    return found

def display_product(name, price, units):
  print(f"Name: {name}, Price: ${price}, Count: {units}, Total: ${format(float(price) * int(units), '.2f')}")

def add_item(name, price, units):
  nextId = int(inventory[-1][0]) + 1
  file = open(path, "a")
  file.write(f"\n{nextId},{name},{price},{units}")
  print(f"{name} added to products.txt!")

def update_inventory(name, units_sold, inventory):
  for item in inventory:
    for entry in item:
      if name in entry:
        if units_sold <= int(item[3]):
          # update the inventory in the list in place
          item[3] = str(int(item[3]) - units_sold)
          return over_write(inventory)
        else:
          return print("not enough units in stock.")
  return print("product not found.")

def over_write(inventory):
  # Clear the entire file first
  clear = open(path, "w")
  clear.write("")
  # Then append the updated inventory
  file = open(path, "a")
  for item in inventory:
    item = ",".join(item) + "\n"
    file.write(item)
  print("inventory updated!")
  file.close()
  clear.close()



""" GAME PLAY: """

ans = "Y"

while ans != "N":
  inventory = load_path(path)
  query = ""
  while (len(query) <= 0):
    query = (input("search for a product: ")).title()
  search(query)
  ans = (input("\nOptions:\n1: Search again \n2: Add an item \n3: Update inventory \nN: Quit \n:")).capitalize()
  if ans == "1":
    continue
  elif ans == "2":
    name = input("Name of item to add: ").title()
    price = input("Price: $")
    units = input("Number of units: ")
    add_item(name, price, units)
  elif ans == "3":
    name = input("Name of item to update: ").title()
    units_sold = int(input("Units to remove: "))
    update_inventory(name, units_sold, inventory)
  else:
    print("invalid input.")
    continue