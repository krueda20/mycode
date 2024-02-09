#!/usr/bin/env python3

def show_activity_examples(activity):
    if activity == "Reading":
        print("Examples of reading materials:")
        print("- Fiction novels")
        print("- Non-fiction books")
        print("- Magazines or articles")
    elif activity == "Brain activity":
        print("Examples of brain-stimulating activities:")
        print("- Puzzles (crosswords, Sudoku)")
        print("- Brain teasers")
        print("- Learning a new language")
    elif activity == "Fun games":
        print("Examples of fun games:")
        print("- Board games (Monopoly, Scrabble)")
        print("- Video games")
        print("- Card games (Uno, Poker)")
    elif activity == "TV":
        print("Examples of TV shows or movies:")
        print("- Comedy series")
        print("- Thrillers")
        print("- Documentaries")
    else:
        print("Unknown activity. Please choose from the provided options.")

def boredom_tracker():
    while True:
        bored_response = input("Are you bored? (yes/no): ").lower()

        if bored_response == "yes":
            print("Do any of these sound fun?")
            activities = ["Reading", "Brain activity", "Fun games", "TV"]
            for i, activity in enumerate(activities, start=1):
                print(f"{i}. {activity}")

            choice = input("Enter the number corresponding to the activity you'd like to do: ")
            try:
                choice = int(choice)
                if 1 <= choice <= len(activities):
                    selected_activity = activities[choice - 1]
                    print(f"Great choice! You selected {selected_activity}.")
                    show_activity_examples(selected_activity)
                else:
                    print("Invalid choice. Please select a valid activity.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif bored_response == "no":
            print("Alright, have a great day!")
            break
        else:
            print("Invalid response. Please answer with 'yes' or 'no.'")

if __name__ == "__main__":
    boredom_tracker()

