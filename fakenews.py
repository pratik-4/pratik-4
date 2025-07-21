import random
subjects=[
  "Salman Khan",
  "Sahrukh Khan",
  "Kartik Aryan",
  "Narendar modi",
  "Virat Kholi",
  "MS Dhoni",
  "Varun Dhawan",
  "Akshay Kumar",
  "yuvraj singh",

]
actions=[
    "Launches",
    "cancels",
    "eating",
    "dancing with",
    "romaing in street with",
    "takes gift from",
    "declares war on",
    "orders with",
    "Ceelebrates"


]
places_or_things=[
  "at Red Fort",
  "in Mumbai Local train",
  "a plate of samosa",
  "a palte of fruits",
  "a cup of cofee",
  "at charminar",
  "in jungle",
  "during ipl match"
]
while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    place_or_thing=random.choice(places_or_things)


    headline=(f"Breaking News:: {subject} {action} {place_or_thing}")
    print("\n"+headline)


    user_input=input("\n Do You WAnt another headlines(yes/no)".strip().lower())
    if user_input=="no":
        break

print("\n Thanks for using the Fake News HEadlines Generators..")