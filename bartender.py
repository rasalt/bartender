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

def main():
  c_drink = {}
  ing_list = []
  c_drink = ask_drink(questions)
  ing_list = construct_drink(ingredients, c_drink)
  if ing_list:
    print "Your drink contains all this cool stuff \n" 
    for ing in ing_list:  
      print "{}".format(ing)
  
if __name__ =='__main__':
  main()                    
                    
                    