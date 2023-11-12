#!/usr/bin/env python
#Verb Conjugator for French by @Eylul 2023
#Conjugate French verbs in the Present Tense
#Version 0.1
#When I learn Python better, I will add more functions to this program.
#I will add more tenses and more verbs. And also save in various formats

import os
import time
from time import sleep

print("\n")
def banner():
    print("\033[32m*""*\033[0m"*33) 
    print("\n")
    sleep(0.3)
    print("Hi, to all beginner level French learners like me.\033") 
    sleep(0.5)
    print("\033[34mI am Eylul. I try to learn French by practising Python as well.")
    sleep(1)
    print("     ")
    print("\033[32m\t\t    Verb Conjugator for French by Eylul\033[0m")
    sleep(1)
    print("\033[34m\t\tConjugate French verbs in the Present Tense\033[0m") 
    sleep(1)
    print("\033[37m\t\t\t\tVersion 0.1\n\033[0m")
    print("\033[32m*""*\033[0m"*33)

banner()

print("")
sleep(0.5)

# Define a function to conjugate French verbs in the present tense
def conjugate_verb(verb):
    # Define the verb endings for each subject pronoun
    endings = {
        "je": "e",
        "tu": "es",
        "il/elle/on": "e",
        "nous": "ons",
        "vous": "ez",
        "ils/elles": "ent"
    }
    
    # Split the verb into its stem and ending
    stem = verb[:-2]
    ending = verb[-2:]
    
    # Check if the verb is a regular -er verb
    if ending == "er":
        # Conjugate the verb using the regular -er verb endings
        conjugations = {
            "je": stem + "e",
            "tu": stem + "es",
            "il/elle/on": stem + "e",
            "nous": stem + "ons",
            "vous": stem + "ez",
            "ils/elles": stem + "ent"
        }
    else:
        # Conjugate the verb using the appropriate irregular verb endings
        if ending == "ir":
            stem = stem + "iss"
        elif ending == "re":
            stem = stem[:-1]
        
        conjugations = {}
        for subject, ending in endings.items():
            conjugations[subject] = stem + ending
    
    # Return the conjugations as a dictionary
    return conjugations

# Test the function with some example verbs 
verbs = ["parler", "finir", "aller", "aimer", "prendre", "vivre", "être", "avoir", "faire", "dire", "pouvoir", "savoir", "venir", "voir", "falloir", "devoir", "mettre", "trouver", "donner", "passer", "jeter", "manger", "boire", "chanter", "dormir", "écouter", "regarder", "lire", "écrire", "acheter", "vendre"] 

# Ask the user if they want to save the output to a txt file
try:
    save_to_file = input("\033[31mDo you want to save the output to a txt file? (y/n): \033[0m")
    sleep(0.1)
    print("\nYou can give any name - Example:  Verb Conjugations.txt")
    sleep(0.1)
    print("If you don't want to save, just press enter.")
    sleep(0.1)
    print("If you want to save, please enter y or Y.")
    sleep(0.1)
    print("Verbs are saved in the same folder as the program.")
    print("\n\t\033[34mVerbs: \033[94m") 

    if save_to_file.lower() == "y":
        # Create a new file to save the output
        filename = input("\nEnter the name of the file: ")
        sleep(0.1)

        with open(filename, "a") as f:
            for verb in verbs:
                f.write("\n" + verb + "\n")
                f.write(str(conjugate_verb(verb)) + "\n")
        if save_to_file.lower() == "y":
            # Create a new file to save the output. So user can study later.  
            filepath = os.path.join(os.path.dirname(__file__), filename)
            with open(filepath, "w") as f:
                f.write("\n" 'Verb Conjugations in French' "\n")
                for verb in verbs:
                    f.write("\n" + verb + "\n")
                    f.write(str(conjugate_verb(verb)) + "\n")
                    sleep(0.1)
            print("\nVerb Conjugations were saved to ", filepath)
    else:
        # Print the output to the console
        for verb in verbs:
         print("\n" + verb)
    print("\n\033[33mExample Verb Conjugations in French\n\033[0m") 
    for verb in verbs:
        print(conjugate_verb(verb))
    print("\n\033[31mExitting...Goodbye!\n\033[0m") 
except KeyboardInterrupt:
    print("\nProgram stopped by user (Ctrl+C)\n")

    print("Goodbye!")
    sleep(0.1)
    exit()
except Exception as e:
    print("\nAn unknown error occurred")
    print(e)
    sleep(0.1)
    exit()

