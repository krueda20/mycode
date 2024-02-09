#!/usr/bin/env python3
"""Challenge | exploring different
   uses of dictionaries"""
# Define the dictionary of Marvel characters
marvelchars = {
    "Starlord": {
        "real name": "peter quill",
        "powers": "dance moves",
        "archenemy": "Thanos"
    },
    "Mystique": {
        "real name": "raven darkholme",
        "powers": "shape shifter",
        "archenemy": "Professor X"
    },
    "Hulk": {
        "real name": "bruce banner",
        "powers": "super strength",
        "archenemy": "adrenaline"
    }
}

# Get user input for character name and statistic
char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk): ")
char_stat = input("What statistic do you want to know about? (real name, powers, archenemy): ")

# Retrieve the value from the dictionary
if char_name in marvelchars and char_stat in marvelchars[char_name]:
    value = marvelchars[char_name][char_stat]
    print(f"{char_name}'s {char_stat} is: {value}")
else:
    print("Invalid character name or statistic. Please check your input.")








