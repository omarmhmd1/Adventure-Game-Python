# Import Time Module to Create Sleeping
import time
# Import Random
import random


# Function for print and then sleep
def print_pause(
        text):
    print(text)
    time.sleep(2)

# -------------------------------------------------------


# Function takes the choice from player
def take_the_choice():
    choice = input("Press (1 or 2) : ")
    while choice not in ["1", "2"]:
        choice = input("Please, Press (1 or 2) : ")
    return choice


# Function asks player for play again
def ask_play_again():
    try_again = input("Do you want play again [y/n] : ")
    while try_again.lower() not in ["y", "n"]:
        try_again = input("Pleas enter [y/n] : ")
    return try_again.lower()


# Function shows game over message
def game_over():
    state = False
    print("Thank you, we hope enjoyed it.")
    return state

# -------------------------------------------------------


# Function starts the game
def describe_what_happen():
    # Print Welcome and Description
    print_pause("\nWelcome To Adventure World - Space Adventure !\n")
    print_pause("While you were at the Earth Alien Protection Center")
    print_pause("you received a message saying : that aliens are planning")
    print_pause("to invade Earth by inventing a laser-powered cannon.")
    print_pause("Once this plan is complete,")
    print_pause("the Laser Cannon will be aimed")
    print_pause("at Earth, and in an instant, ")
    print_pause("the planet will be reduced to ash")
    print_pause("Then, You said to yourself :\n")
    # Show choices from player
    print_pause("1- Will I confront them and defeat them?")
    print_pause("2- Will I leave it to someone else with their team?")
    return take_the_choice()


# Function if player chooses to save world and go to attack aliens
def choose_saving_world(
        color_of_first_planet, color_of_second_planet):
    print_pause("That is true! Let's go to ride")
    print_pause("a Spacecraft that moves very quickly")
    print_pause("As you were going to aliens, You saw two Planets, ")
    print_pause(f"the first was {color_of_first_planet},")
    print_pause(f"the other was {color_of_second_planet}, Oh no !")
    print_pause("the aliens started attacking us using laser defenses.")
    print_pause("What do I do ?", )


# Function if player chooses to leave it the task for
# someone else and their team and the tries are zero
def decision_staying_tries_zero():
    print_pause("You decided to stay and leave the task for")
    print_pause("someone else and their team")
    print_pause("But the another person couldn't succeed in it !")
    print_pause("Oh no ! the aliens fired a laser beam and the")
    print_pause("earth would turn to ash..\nYou Lose")
    return ask_play_again()


# Function if player chooses to leave it the task for
# someone else and their team the tries aren't zero
def decision_staying_tries_not_zero():
    print_pause("You decided to stay and leave the task for person else")
    print_pause("But the another person couldn't succeed in it !")
    print_pause("But there is another chance before aliens")
    print_pause("fire a laser beam and the earth would turn to ash..")
    print_pause("1- Will I confront them and defeat them?")
    print_pause("2- Will I leave it to someone else with their team")
    return take_the_choice()


# -------------------------------------------------------


# Function if player chooses to land on first planet
def landing_on_first_planet(
        monsters):
    print_pause("You decided to land on the first planet,")
    print_pause(f"Then, You saw {monsters} guard the energy building")
    print_pause("that makes energy for big and huge Laser Cannon")
    print_pause("What do you want to do ?")
    print_pause("1- Attack them and blow up the energy building")
    print_pause("2- Back to space where you found the safe place")
    return take_the_choice()


# Function if player chooses to land on second planet
def landing_on_second_planet(
        found):
    # Check if player goes first time or no
    if found is False:
        print_pause("You landed safely on a second planet,")
        print_pause("then you get out of the spacecraft,")
        print_pause("angry that you couldn't defeat the aliens and")
        print_pause("slam your leg into the dirt in anger.")
        print_pause("Here's the surprise! You accidentally hit a")
        print_pause("machine's operating lever")
        print_pause("and a building appears containing more than")
        print_pause("100 automated spacecraft operating\nWow!")
        print_pause("1- Will you turn on those automated spacecraft")
        print_pause("2- Back to space where you found the safe place")
        return take_the_choice()
    else:
        print_pause("You went to second planet")
        print_pause("You did not see any new thing")
        print_pause("You saw the building containing more than")
        print_pause("100 automated spacecraft operating")
        print_pause("1- Will you turn on those automated spacecraft")
        print_pause("2- Back to space where you found the safe place")
        return take_the_choice()


# ------------------------------------------------------


# Function if player chooses to attack them and blow up the energy building
def attack_and_blow_up(
        power, monster):
    # Check from Power
    if power >= 70:
        print_pause("You turned on them and went to the first planet")
        print_pause(f"You saw {monster} around the energy building")
        print_pause("You started attacking with your automated")
        print_pause("spacecrafts, Cool, We are about to defeat them,")
        print_pause("We did it, We defeated enemy")
        print_pause("But the Laser Cannon is still has energy source")
        print_pause("Let's go to the planet contains")
        print_pause("Big and Huge Laser Cannon\n")
        return "success"

    elif 25 < power < 70:
        print_pause("You started attacking them, But they were stronger")
        print_pause("than you, So you couldn't defeat them and you")
        print_pause("escaped to safe place on the planet")
        print_pause("1- Back again and attack them")
        print_pause("2- Back to space where you found the safe place")
        return take_the_choice()

    elif power <= 25:
        print_pause("You started attacking, No, the power of")
        print_pause("your spacecraft is too weak")
        print_pause("Oh No, They defeated your spacecraft and catch you, ")
        print_pause("You Lose!")
        return ask_play_again()


# -------------------------------------------------------


# Function asks player which planet player will go to it
def go_to_first_or_second_planet():
    print_pause("You went to safe area in space,")
    print_pause("And you still seeing the same planets")
    print_pause("Which planet will you go to?")
    print_pause("1- First Planet")
    print_pause("2- Second Planet")
    return take_the_choice()


# Function if player reaches the planet contains Laser Cannon
def reaches_the_laser_cannon():
    print_pause("Cool, Let's go to attack! You and the")
    print_pause("automated spacecrafts went, Let's to defeat the Cannon")
    print_pause("You saw the Laser Cannon, It was big and huge")
    print_pause("-To Defeat the cannon, You must answer the puzzle-")
    print_pause("the system of cannon said it\n")
    print_pause("The Puzzle : -A snail climbs a 20-meter-high wall every day,")
    print_pause("It climbs two meters during the day and")
    print_pause("descends one meter at night to be able to pull-\n")
    print_pause("How many days does it take for")
    print_pause("a snail to reach the top of the wall ?")
    print_pause("1-20 \n2-19 \n3-21 ")
    puzzle_answer = input("Press (1 , 2 or 3) : ")
    while puzzle_answer not in ["1", "2", "3"]:
        puzzle_answer = input("Please, Press (1 , 2 or 3) : ")
    return puzzle_answer


# -------------------------------------------------------


# Function if player solves the puzzle
def solve_puzzle():
    print_pause("Hold on, the cannon is about to explode")
    print_pause("Three,")
    print_pause("Two,")
    print_pause("One,")
    print_pause("BOOM")
    print_pause("Yes, We did it, You're Victorious!")


# Function if player couldn't solve the puzzle
def not_solve_puzzle():
    print_pause("Wrong Solution, Shot on the Earth")
    print_pause("No, You Lose !")
    return ask_play_again()


# Function increases or decreases the total score
# and print total score
def print_total_score(total_score, points):
    total_score += points
    print_pause("\n" + str(points) + " points\n")
    print_pause("You Total Score : " + str(total_score))
    return total_score


# -------------------------------------------------------


# Main Function that start the game and continue the story
def main():

    # Random color for first planet and second planet
    color_of_first_planet = random.choice(["blue", "purple", "green-blue"])
    color_of_second_planet = random.choice(["red", "orange", "brown"])
    # Random Monster
    monsters = random.choice(["aliens", "Ground Monsters", "Laser Cannons"])

    # The state of game
    state_of_game = True
    # number of tries for try saving the world
    tries = 3
    # The value of power to defeat the monster
    power = 50
    # found the automated spacecrafts
    found = False
    # Total Score
    total_score = 20

    # Is function (save world) call
    is_choose_saving_world_function_call = False

    # Print Welcome and Description
    first_choice = describe_what_happen()
    while state_of_game is True:
        # Scenario 1 - War Aliens or Leave the Task

        # Correct choice - Go And Attack
        if first_choice == "1":

            # Scenario 2 - Land on First Planet or Second Planet
            # Show going to spacecraft and Increase Score but once
            if is_choose_saving_world_function_call is False:
                # Increase Score
                total_score = print_total_score(total_score, 15)
                choose_saving_world(color_of_first_planet,
                                    color_of_second_planet)

                is_choose_saving_world_function_call = True

            # Variable has the choice go to first or second planet
            land_on_first_or_second = go_to_first_or_second_planet()

            # Correct choice - Landing on Second Planet
            if land_on_first_or_second == "2":

                # Increase Score
                total_score = print_total_score(total_score, 10)

                # Scenario 3 - Turn the Automated Spacecraft or
                # Back to Area where it is safe

                choice_second_planet = landing_on_second_planet(found)
                found = True

                # Correct Choice - Turn the Automated Spacecrafts
                if choice_second_planet == "1":

                    # Increase Score
                    total_score = print_total_score(total_score, 20)

                    # Scenario 4 - Attack and Solve or not Solve the puzzle
                    power += 50
                    attack_and_blow_up(power, monsters)
                    # Variable has the choice of the puzzle
                    puzzle_answer = reaches_the_laser_cannon()

                    # Puzzle Answer - Correct Choice
                    if puzzle_answer == "2":
                        solve_puzzle()
                        # Increase Score
                        total_score = print_total_score(total_score, 25)

                        # Solve Puzzle and play again - yes or no
                        play_again = ask_play_again()
                        if play_again.lower() == "y":
                            first_choice = describe_what_happen()
                        else:
                            state_of_game = game_over()

                    # Puzzle Answer - incorrect Choice
                    else:
                        # Decrease Score
                        total_score = print_total_score(total_score, -10)

                        # Not Solve Puzzle and play again - yes or no
                        play_again = not_solve_puzzle()

                        if play_again.lower() == "y":
                            first_choice = describe_what_happen()
                        else:
                            state_of_game = game_over()

                # Incorrect Choice - Back to the safe space area
                else:
                    # Decrease Score
                    total_score = print_total_score(total_score, -5)

                    print_pause("You returned to the safe space area")
                    continue

            else:
                # Decrease Score
                total_score = print_total_score(total_score, -15)

                # Scenario 5
                # Attack the Monsters or Back to Area where it is safe
                choice_first_planet = landing_on_first_planet(monsters)

                # Correct Choice - Back to Area where it is safe
                if choice_first_planet == "2":
                    # Increase Score
                    total_score = print_total_score(total_score, 10)

                    print_pause("You decided to return to")
                    print_pause("the safe space area")
                    continue

                # Attack the monsters - Incorrect Choice
                else:
                    # Decrease Score
                    total_score = print_total_score(total_score, -10)

                    power -= random.choice([15, 5, 10])
                    choice_attack = attack_and_blow_up(power, monsters)

                    # Attack the Monster until player chooses attack them
                    while choice_attack == "1":
                        # Decrease Score
                        total_score = print_total_score(total_score, -10)

                        power -= random.choice([15, 5, 10])
                        choice_attack = attack_and_blow_up(power, monsters)

                        # Check the power and show score
                        if power <= 20:
                            print_pause("Your Score : " + str(total_score))

                    # Increase Score
                    total_score = print_total_score(total_score, 5)

                    # Try Again
                    if choice_attack.lower() == "y":
                        tries = 3
                        total_score = 20
                        found = False
                        is_choose_saving_world_function_call = False
                        first_choice = describe_what_happen()
                    elif choice_attack.lower() == "n":
                        state_of_game = game_over()

        # Incorrect Choice - Leave the task
        elif first_choice == "2":

            # Decrease Score
            total_score = print_total_score(total_score, -5)

            # Try Again
            # If his tries is zero
            if tries == 0:
                try_again = decision_staying_tries_zero()
                if try_again.lower() == "y":
                    tries = 3
                    total_score = 20
                    found = False
                    is_choose_saving_world_function_call = False
                    first_choice = describe_what_happen()
                elif try_again.lower() == "n":
                    state_of_game = game_over()

            # If his tries is greater than zero
            else:
                tries -= 1
                first_choice = decision_staying_tries_not_zero()


if __name__ == "__main__":
    main()
