import json

import json

dog_data = {
  "name": "Frieda",
  "is_dog": True,
  "hobbies": ["eating", "sleeping", "barking"],
  "age": 8,
  "address": {
    "work": None,
    "home": ("Berlin", "Germany",),
  },
  "friends": [
    {
      "name": "Philipp",
      "hobbies": ["eating", "sleeping", "reading",],
    },
    {
      "name": "Mitch",
      "hobbies": ["running", "snacking"],
    },
  ],
}

with open("save_file.json", mode="w",encoding="utf-8") as write_file:
    json.dump(dog_data, write_file, indent=3)

with open("save_file.json", mode="r", encoding="utf-8") as read_file:
    new_dog = json.load(read_file)

print(type(new_dog)) #dict