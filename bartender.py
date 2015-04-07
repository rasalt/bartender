#!/usr/bin/python
#Questions to ask each customer or after every drink

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
} 
import random
def construct_drink(ingredients, customer_drink):
  i_list = []
  for type, liked in customer_drink.iteritems():
#   print choice
    if liked:
#     print random.choice(ingredients[choice]) 
      i_list.append(random.choice(ingredients[type]))
  return i_list    
  
def ask_drink(questions):
  customer_drink = {}
  for type, question in questions.iteritems():
    print question
    customer_drink[type] = raw_input().lower() in ['y', 'yes']
  print customer_drink  
  return customer_drink

adj = ["cuddly", "furry", "yellow","dirty","bloody","hairy","naughty"]
noun = ["seadog", "tiger","puppy", "tarantula", "sealion","hippo","tuna","shark"]
name_dir = {}

def get_uniquedrinkname(i_list):
  name = random.choice(adj)+" "+random.choice(noun)
  while name in name_dir:
    name = random.choice(adj)+" "+random.choice(noun)
  #Add to the name directory
  name_dir[name] = i_list
  print "Name director is now {} ".format(name_dir)
  return name
  
def getdrinkname(i_list):
  #Search the ingredients list in the name directory  
  for name, ing in name_dir.iteritems():
    if ing == i_list:
      return name
  newname = get_uniquedrinkname(i_list)
  return newname

person_drink = {}
def main():
  another = True
  while another:
    c_drink = {}
    ing_list = []
    print "Could I have your name please for the order ?"
    person = raw_input().lower()
    if person in person_drink:
      print "Would you like the same as the last or a new one ? "
      same = raw_input().lower() in ['s', 'same']
      if same:
        ing_list = person_drink[person]
    else:
        c_drink = ask_drink(questions)
        ing_list = construct_drink(ingredients, c_drink)
    if ing_list:
  #   Create name and add it to the name dictionary
      drinkname = getdrinkname(ing_list)
      person_drink[person] = ing_list;
      print "\n {} :Your drink {} contains all this cool stuff \n".format(person, drinkname).upper() 
      for ing in ing_list:  
        print "{}".format(ing)

    print "Would you like a drink  ? "    
    another = raw_input().lower() in ['y','yes']
      
    
if __name__ =='__main__':
  main()                    
                    
                    