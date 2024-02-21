#!/usr/bin/env python3
"""My way of using my recommendations so I dont have to keep track of all my activities 
I dont want to scroll through all my recommednations when Im bored I just want something to do"""


def boredomplsgoaway():
    print("Welcome to the Boredom Buster Menu!")
    print("Let's find something fun to do. Answer the following questions:")

    while True:
        bored = input("Are you bored? (yes/no): ").lower()
        if bored == "no":
            print("Okay then, get busy!")
            break
        elif bored == "yes":
            print("What sounds fun right now?")
            print("1. Brain stimi")
            print("2. Physical Stimi")
            print("3. Lazy Stimi")
            print("4. Reading")
            choice = input("Enter the number corresponding to your choice: ")

            if choice == "1": #Brain stimi
                print("Which one sounds the most fun?")
                print("a. Crossword")
                print("b. Sudoku")
                print("c. New language")
                print("d. Word search")
                brain_choice = input("Enter the letter corresponding to your choice: ")
                if brain_choice == "a": #crossword
                    print("Select which crossword you want to do:")
                    print("1. Website")
                    print("2. Phone game")
                    print("3. Booklet")
                    crossword_choice = input("Enter the number corresponding to your choice: ")
                    if crossword_choice == "1":
                        print("Enjoy solving crosswords online!")
                    elif crossword_choice == "2":
                        print("Pull out your phone and have fun solving")
                    elif crossword_choice == "3":
                        print("Grab a crossword booklet and challenge yourself")
                    else:
                        print("I think I am missunderstanding try again!")
                elif brain_choice == "b": # sudoku
                    print("Select which sudoku you want to do:")
                    print("1. Website")
                    print("2. Phone game")
                    print("3. Booklet")
                    Sudoku_choice = input("Enter the number corresponding to your choice: ")
                    if Sudoku_choice == "1":
                        print("Enjoy solving sudoku online!")
                    elif Sudoku_choice == "2":
                        print("Pull out your phone and have fun solving")
                    elif Sudoku_choice == "3":
                        print("Grab a sudoku booklet and challenge yourself")
                    else:
                        print("I think I am missunderstanding try again!")
                elif brain_choice == "c": # New Language
                    print("Have fun learning Duo lingo!")
                elif brain_choice == "d": # word search
                    print("Select which word search you want to do:")
                    print("1. Website")
                    print("2. Phone game")
                    print("3. Booklet")
                    wordsearch_choice = input("Enter the number corresponding to your choice: ")
                    if wordsearch_choice == "1":
                        print("Enjoy solving word search online!")
                    elif wordsearch_choice == "2":
                        print("Pull out your phone and have fun solving")
                    elif wordsearch_choice == "3":
                        print("Grab a wordsearch booklet and challenge yourself")
                    else:
                        print("I think I am missunderstanding try again!")
                    
                else:
                    print("Invalid choice. Please try again.")

            elif choice == "2": # physical stimi
                print("Which one sounds the most fun?")
                print("a. Board game")
                print("b. Slime")
                print("c. Puzzle")
                print("d. Coloring")
                physical_choice = input("Enter the letter corresponding to your choice: ")
                if physical_choice == "a": # board game Never have I ever, truth or dare, What's your sign, Monopoly
                    print("Select Which board game you want to play")
                    print("1. Never have I ever")
                    print("2. Truth or Dare")
                    print("3. What's your sign")
                    print("4. Monopoly")
                    boardgame_choice = input("Enter the number corresponding to your choice: ")
                    if boardgame_choice == "1":
                        print("Well get to it")
                    elif boardgame_choice =="2":
                        print("Hope you choose dare")
                    elif boardgame_choice == "3":
                        print("I bet you are an aries")
                    elif boardgame_choice == "4":
                        print("What are you waitng for? Go Monoplay")
                    else: 
                        print("I think you have made a mistake. Try again")

                elif physical_choice == "b": # slime Coal, Dirt, Snowbuddy
                    print("Select which goo you want?")
                    print("1. Coal")
                    print("2. Dirt")
                    print("3. Snowbuddy")
                    print("4. Paper Rings")
                    slime_choice = input("Enter the number corresponding to your choice: ")
                    if slime_choice == "1":
                        print("Go play with Santas gift")
                    elif slime_choice =="2":
                        print("Get diggin!")
                    elif slime_choice == "3":
                        print("Go build a Snowman!")
                    elif slime_choice == "4":
                        print("Maybe listen to some Taylor while you play")
                    else:
                        print("Maybe you got your options mixed up! Try again!")

                elif physical_choice == "c": # Puzzle Rubrix cube, jigsaw puzzle,
                    print("What kind of puzzle are you in the modd for?")
                    print("1. Rubrix cube")
                    print("2. Jigsaw puzzle")
                    puzzle_choice = input("Enter the number corresponding to your choice: ")
                    if puzzle_choice == "1":
                        print("How fast can you solve that cube?")
                    elif puzzle_choice == "2":
                        print("Go solve that mystery")
                    else:
                        print("Maybe puzzles are not what you were in the mood for afterall?")

                elif physical_choice == "d": # Coloring Paint by number, Children coloring book, or adult coloring book Congrats Go color like a rainbow
                    print("Which coloring option sounds good?")
                    print("1. Paint by number")
                    print("2. Childrens coloring book")
                    print("3. Adult Coloring book")
                    coloring_choice = input("Enter the number corresponding to your choice: ")
                    if coloring_choice == "1":
                        print("Get the cup of water and paint brush")
                    elif coloring_choice == "2":
                        print("I bet there are princesses that need a hint of color")
                    elif coloring_choice == "3":
                        print("I bet there is a lot of shapes that need some colors")
                    else:
                        print("I am not quite understanding, try again")

                else:
                    print("Invalid choice. Please try again.")

            elif choice == "3": # Lazy Stimi- Movie, Show, Social Media, or Nap
                print("Which one sounds the most fun?")
                print("a. Movie")
                print("b. Show")
                print("c. Social Media")
                print("d. Nap")
                lazy_choice = input("Enter the letter corresponding to your choice: ")
                if lazy_choice == "a": #Movie- Comedy, Horror, Romance/Drama, Action, Series
                    print("What genre are you feeling?")
                    print("1. Comedy")
                    print("2. Horror")
                    print("3. Romance/Drama")
                    print("4. Action")
                    print("5. Sagas")
                    movie_choice = input("Enter the number corresponding to your choice: ")
                    if movie_choice == "1": #Comedy
                        print("But which comedy?")
                        print("a. The Decoy Bride")
                        print("b. Joy Ride")
                        print("c. Holdovers")
                        print("d. No Hard Feelings")
                        print("e. Glass Onion")
                        comedy_choice = input("Enter the letter corresponding to your choice: ")
                        if comedy_choice == "a":
                            print("Hope you have a laugh")
                        elif comedy_choice == "b":
                            print("Hope you have a laugh")
                        elif comedy_choice == "c":
                            print("Hope you have a laugh")
                        elif comedy_choice == "d":
                            print("Hope you have a laugh")
                        elif comedy_choice == "e":
                            print("Hope you have a laugh")
                        else:
                            print("Oops i do not understand, Try again!!")
                    elif movie_choice == "2": #Horror
                        print("But how scary?")
                        print("a. Theory of Everything")
                        print("b. Imitation Game")
                        print("c. God help the Girl")
                        print("d. Dunkirk")
                        print("e. Brooklyn")
                        horror_choice = input("Enter the letter corresponding to your choice: ")
                        if horror_choice == "a":
                            print("Hope you have a good scare")
                        elif horror_choice == "b":
                            print("Hope you have a good scare")
                        elif horror_choice == "c":
                            print("Hope you have a good scare")
                        elif horror_choice == "d":
                            print("Hope you have a good scare")
                        elif horror_choice == "e":
                            print("Hope you have a good scare")
                        else:
                            print("Oops i do not understand, Try again!!")
                    elif movie_choice == "3": #Romance/Drama
                        print("But which Romance/Drama?")
                        print("a. Kiss Me")
                        print("b. Just Friends")
                        print("c. The Notebook")
                        print("d. Dirty Dancing")
                        print("e. Brokeback Mountain")
                        romance_choice = input("Enter the letter corresponding to your choice: ")
                        if romance_choice == "a":
                            print("Hope you have a chuckle")
                        elif romance_choice == "b":
                            print("Hope you find hope in love again")
                        elif romance_choice == "c":
                            print("Hope you find love")
                        elif romance_choice == "d":
                            print("Hope you have a little cry")
                        elif romance_choice == "e":
                            print("Hope you have a good cry")
                        else: 
                            print("Oops i do not understand, Try again!!")
                    elif movie_choice == "4": #Action
                        print("But which Action?")
                        print("a. Interstellar")
                        print("b. Everything Everywhere all at Once")
                        print("c. RED")
                        print("d. Jumanji")
                        print("e. Super 8")
                        action_choice = input("Enter the letter corresponding to your choice: ")
                        if action_choice == "a":
                            print("Hope you are sitting on the edge of your chair")
                        elif action_choice == "b":
                            print("Hope you are sitting on the edge of your chair")
                        elif action_choice == "c":
                            print("Hope you are sitting on the edge of your chair")
                        elif action_choice == "d":
                            print("Hope you are sitting on the edge of your chair")
                        elif action_choice == "e":
                            print("Are you ready to sit on the edge of your seat")
                        else: 
                            print("Oops i do not understand, Try again!!")
                    elif movie_choice == "5": #Saga
                        print("But which Sagas?")
                        print("a. Star trek")
                        print("b. The Mummy")
                        print("c. Indiana Jones")
                        print("d. Alien")
                        print("e. Jurassic Park")
                        saga_choice = input("Enter the letter corresponding to your choice: ")
                        if saga_choice == "a":
                            print("Here is a launch to space")
                        elif saga_choice == "b":
                            print("You might need some toilet paper")
                        elif saga_choice == "c":
                            print("Get your rope and whips ready!")
                        elif saga_choice == "d":
                            print("Get on the spaceship and prepare to take off!")
                        elif saga_choice == "e":
                            print("Dinos sounds fun but maybe not these!")
                        else:
                            print("Oops i do not understand, Try again!!")
                    else: 
                        print("Maybe a movie is not your vibe?")

                elif lazy_choice == "b": #show- Gresy Anatomy, The Office, RuPauls Dragrace, Criminal Minds, Psych
                    print("Which show sounds like the most comforting?")
                    print("1. Greys Anatomy")
                    print("2. The Office")
                    print("3. Rupaul's Drag Race")
                    print("4. Criminal Minds")
                    print("5. Psych")
                    show_choice = input("Enter the number corresponding to your choice: ")
                    if show_choice == "1":
                        print("If you pay close enough attention you'll learn how to do a whipple")
                    elif show_choice == "2":
                        print("Have a good laugh")
                    elif show_choice == "3":
                        print("Shantay you better werk")
                    elif show_choice == "4":
                        print("Enjoy the cases and try not to cry")
                    elif show_choice == "5":
                        print("Don't forget to send updates to your gf")
                    else: 
                        print("Maybe a show isnt fitting the vibe? Try again")
                elif lazy_choice == "c":#Social Media- Instagram, Tiktok, Facebook, or Twitter
                    print("What vibe of scrolling do you want?")
                    print("1. Instagram")
                    print("2. Tiktok")
                    print("3. Facebook")
                    print("4. Twitter")
                    socials_choice = input("Enter the number corresponding to your choice: ")
                    if socials_choice == "1":
                        print("Go stalk Taylor or your gf")
                    elif socials_choice == "2":
                        print("Just set a timer so you do not get into a doom of scrolling")
                    elif socials_choice == "3":
                        print("Have fun scrolling you Millenial!")
                    elif socials_choice == "4":
                        print("Check on the seceret songs today?")
                    else:
                        print("Scrolling not the feeling your chasing? Try again")
                elif lazy_choice == "d": # Nap
                    print("Have sweet sweet dreams!")
                else:
                    print("Invalid choice. Please try again.")

            elif choice == "4": # Reading- Book, Poetry, Short story, or News article
                print("Which one sounds the most fun?")
                print("a. Book")
                print("b. Poetry")
                print("c. Short Story")
                print("d. News article")
                reading_choice = input("Enter the letter corresponding to your choice: ")
                if reading_choice == "a": # Book- Historical Fiction, Fantasy, Contemporary/Romance, Educational, Series, Mystery, Horror
                    print("What genre fits the vibe today?")
                    print("1. Historical Fiction")
                    print("2. Fantasy")
                    print("3. Contemporary/Romance")
                    print("4. Educational")
                    print("5. Mystery")
                    print("6. Horror")
                    print("7. Series")
                    book_choice = input("Enter the number corresponding to your choice: ")
                    if book_choice == "1":
                        print("Well which HISFIC sounds good?")
                        print("a. All the Light We Cannot See")
                        print("b. Addie la Rue")
                        print("c. Evelyn Hugo")
                        print("d. Frankenstein")
                        print("e. Small Country")
                        hisfic_choice = input("Enter the letter corresponding to your choice: ")
                        if hisfic_choice == "a":
                            print("Have a tissue near by!")
                        elif hisfic_choice == "b":
                            print("Enjoy!")
                        elif hisfic_choice == "c":
                            print("Enjoy!")
                        elif hisfic_choice == "d":
                            print("Enjoy!")
                        elif hisfic_choice == "e":
                            print("Enjoy!")
                        else:
                            print("None of these options fitting your vibe? Maybe try again")
                    elif book_choice == "2": #fantasy
                        print("Well which Fantasy sounds good?")
                        print("a. The Hobbit")
                        print("b. Ninth House")
                        print("c. Under the Whispering")
                        print("d. Howls moving castle")
                        print("e. Jace City")
                        fantasy_choice = input("Enter the letter corresponding to your choice: ")
                        if fantasy_choice == "a":
                            print("Maybe get a snack and Enjoy")
                        elif fantasy_choice == "b":
                            print("Maybe get a snack and Enjoy")
                        elif fantasy_choice == "c":
                            print("Maybe get a snack and Enjoy")
                        elif fantasy_choice == "d":
                            print("Maybe get a snack and Enjoy")
                        elif fantasy_choice == "e":
                            print("Maybe get a snack and Enjoy")
                    elif book_choice == "3":
                        print("Well which Contemporary/Romance sounds good?")
                        print("a. Fly with Me")
                        print("b. The pairing")
                        print("c. Everyone in this Room will Someday be Dead")
                        print("d. Turtles All the Way Down")
                        print("e. All this Could be Different")
                        contemp_choice = input("Enter the letter corresponding to your choice: ")
                        if contemp_choice == "a":
                            print("Enjoy and try not to be devoured by the book!")
                        elif contemp_choice == "b":
                            print("Enjoy and try not to be devoured by the book!")
                        elif contemp_choice == "c":
                            print("Enjoy and try not to be devoured by the book!")
                        elif contemp_choice == "d":
                            print("Enjoy and try not to be devoured by the book!")
                        elif contemp_choice == "e":
                            print("Enjoy and try not to be devoured by the book!")
                        else:
                            print("None of these fitting the vibe? Try again!")
                    elif book_choice == "4": #educational
                        print("which book would you like to learn from today?")
                        print("a. The Body Keeps the Score")
                        print("b. How to Be the Love You Seek")
                        print("c. The Moral Animal")
                        print("d. The Nazi Doctors")
                        print("e. The interpretation of Dreams")
                        edu_choice = input("Enter the letter corresponding to your choice: ")
                        if edu_choice == "a":
                            print("Go learn about Trauma!")
                        elif edu_choice == "b":
                            print("Learn how to heal from your relationships")
                        elif edu_choice == "c":
                            print("Educate yourself on how your psychology affects your decisions!")
                        elif edu_choice == "d":
                            print("Learn about how genocide still is happening!")
                        elif edu_choice == "e":
                            print("What do your dreams mean?")
                        else:
                            print("I do not understand, try again?")
                    elif book_choice == "5": #Mystery
                        print("Which book would you like to dive into today?")
                        print("a. Evelyn Hardcastle")
                        print("b. Sharp Objects")
                        print("c. We were Liars")
                        print("d. Miss Peregrine")
                        print("e. The Strange Case of the Alchemists Daughter")
                        mystery_choice = input("Enter the letter corresponding to your choice: ")
                        if mystery_choice == "a":
                            print("Get your detective feels on!")
                        elif mystery_choice == "b":
                            print("Get your detective feels on!")
                        elif mystery_choice == "c":
                            print("Get your detective feels on!")
                        elif mystery_choice == "d":
                            print("Get your detective feels on!")
                        elif mystery_choice == "e":
                            print("Get your detective feels on!")
                        else:
                            print("Not fitting the vibe? Try another option")
                    elif book_choice == "6": #Horror
                        print("what book would you like to scare you today?")
                        print("a. The Only Good Indians")
                        print("b. I'm thinking of ending Things")
                        print("c. Severance")
                        print("d. Mexican Gothic")
                        print("e. Annihilation")
                        horror_choice = input("Enter the letter corresponding to your choice: ")
                        if horror_choice == "a":
                            print("Hope you get your Thrills on!")
                        elif horror_choice == "b":
                            print("Hope you get your Thrills on!")
                        elif horror_choice == "c":
                            print("Hope you get your Thrills on!")
                        elif horror_choice == "d":
                            print("Hope you get your Thrills on!")
                        elif horror_choice == "e":
                            print("Hope you get your Thrills on!")
                        else:
                            print("Maybe a scare isn't what you are looking for?")
                    elif book_choice == "7": #series
                        print("which World would you like to dive into today?")
                        print("a. Cinder")
                        print("b. Shadow and Bone")
                        print("c. Six of Crows")
                        print("d. The Raven Cycle")
                        print("e. Percy Jackson")
                        series_choice = input("Enter the letter corresponding to your choice: ")
                        if series_choice == "a":
                            print("Dive into the world of Cinder")
                        elif series_choice == "b":
                            print("Dive into the world of Shadow and Bone")
                        elif series_choice == "c":
                            print("Dive into the world of the Six of Crows")
                        elif series_choice == "d":
                            print("Dive into the world of The Raven Cycle")
                        elif series_choice == "e":
                            print("Dive into the world of Percy Jackson")
                        else:
                            print("Maybe commiting to an entire world is not what you are after?")
                    else: 
                        print("Maybe a book isn't what you are looking for?")
                elif reading_choice == "b": # Poetry- Marisas recs or Marisas Poems
                    print("Here are your poetry options")
                    print("1. Marisas Recommendations")
                    print("2. Marisas Poetry")
                    poetry_choice = input("Enter the number corresponding to your choice: ")
                    if poetry_choice == "1": 
                        print("Have fun reading what your gf gave you to read")
                    elif poetry_choice == "2":
                        print("Have fun reading the genius of Marisa")
                    else:
                        print("Poetry not fitting the vibe? Try again?")
                elif reading_choice == "c": # Short Story
                    print("Short stories are perfect for a quick escape. I hear google is a great source for that.")
                elif reading_choice == "d": # News article
                    print("Stay informed with a news article. There are a lot of things this world needs and unbias News is one. Do your part and hear both sides.")
                else:
                    print("Invalid choice. Please try again.")

            else:
                print("Invalid choice. Please try again.")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Call the function to start the menu
boredomplsgoaway()


