from random import randint
from time import sleep

"""
Answers taken from https://en.wikipedia.org/wiki/Magic_8-Ball#Possible_answers
"""

ball_answers = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes definitely.", "You may rely on it.",
                "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
                "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.",
                "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.",
                "Outlook not so good.", "Very doubtful."]
answer_selection = randint(0, 19)


def shake_8ball():
    game_start = True
    while game_start:
        input("Enter your question and hit Enter: ")
        print("Ahh of course...I see...let me think...")
        sleep(1)
        print(ball_answers[answer_selection])
        user_response = input("Would you like to ask another question? Y for Yes, or N for no.")
        user_response = user_response.lower()
        if user_response == 'y':
            return
        else:
            game_start = False


print("Welcome to the Magic 8 Ball! Please, ask it a yes/no question to find your answer!\nKeep in mind, the Magic"
      " 8 Balls power is only so great, so some questions may require asking again.")

shake_8ball()
