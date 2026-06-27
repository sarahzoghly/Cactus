import time 
import pygame
import random
import sys 
import math

pygame.init()

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cactus")

#LISTS
weather = ["stormy", "hot", "unbearable", "freezing", "extremly hot"]
sound = ["a wolf", "the wind", "a strange noise", "a snake"]
food = ["camel meat and bread",
        "sheep meat and bread",
        "plane bread, you are hungry you can't complain",
        "fruit salad",
        "plate of rice",
        "salad",
        "goat cheese",
        "chicken and bread",
        "a strange sandwich, it smells like goat cheese,"
        "lets hope it tastes good.",
        "a coconut slice",
        "a watermelon slice"]

drink = ["warm water",
         "water",
         "cold water",
         "a..smoothie? How did it come here?",
         "orange juice",
         "coctail",
         "coconut water",
         "tea? that may do",
         "green juice.. you are thiristy, you can't complain"]

pet = ["a cat",
       "a parrot",
       "a rabbit",
       "a turtle",
       "a..goat?",
       "a bird",
       "a monkey",
       "a cactus, it may be your imagination"
       "or dehydration but"]

pet_condition =["it looks hungry",
                "it looks like it has a broken bone",
                "it looks like it likes you",
                "it is trying hard to keep up with your wide footsteps",
                "It looks lonely",
                "It is still a baby"]

pet_condition_2 = ["it looks like it loves you now",
                   "it looks hungry",
                   "it is hopping behind you happily"
                   ]

pet_status =["it is asleep, shhhh.",
             "it is tired."
             "it loves you."
             "it is happy."
             "It is happy to be with you.",
             "it is chewing on a random stick on the ground"
             ".. it is an ice-cream stick, yuck.",
             "it is just chilling",
             "it is eating.. your backup food,"
             "it is its now."]

trivia_questions = [
    {"question":"What do you use to write on a blackboard?",
     "answer":"chalk"},
    {"question":"What’s the name of the organ that helps you breathe?",
     "answer":"lung"},
    {"question":"What’s the colored part of your eye called?",
     "answer":"iris"},
    {"question":"What do you call a house made of ice?",
     "answer":"igloo"},
    {"question":"What is the hardest natural substance on Earth?",
     "answer":"diamond"},
    {"question":"What planet is known for its rings?",
     "answer":"saturn"},
    {"question":"What is H2O more commonly known as?",
     "answer":"water"},
    {"question":"What do we call molten rock after it erupts from a volcano?",
     "answer":"lava"},
    {"question":"What part of the body pumps blood?",
     "answer":"heart"},
    {"question":"What tool tells you which direction is north?",
     "answer":"compass"},
    {"question":"In a website browser address bar, what does 'www' stand for?",
     "answer": "world wide web"},
    {"question":"In what year was the Internet opened to the public?",
     "answer": "1993"},
    {"question":"What’s the largest animal on Earth?",
     "answer":"whale"},
    {"question":"What is the largest desert on Earth?",
     "answer":"antarctica"},
    {"question":"What color do you get if you mix red and yellow?",
     "answer":"orange"},
    {"question":"What do cows drink?",
     "answer":"water"},
    {"question":"What season comes after winter?",
     "answer":"spring"},
    {"question":"What has hands but no arms or legs?",
     "answer":"clock"},
    {"question":"What plant is famous for surviving in deserts?",
     "answer":"cactus"},
    {"question":"What animal is known as the 'ship of the desert'?",
     "answer":"camel"},
    {"question":"What’s the main gas in the air we breathe?",
     "answer":"nitrogen"},
    {"question":"What’s the name of the red planet?",
     "answer":"mars"},
    {"question":"What is full of holes but still holds water?",
     "answer":"sponge"},
    {"question":"What’s something you break before you use it?",
     "answer":"egg"},
    {"question":"What language do people speak in Brazil?",
     "answer":"portuguese"},
    {"question":"What fruit has its seeds on the outside?",
     "answer":"strawberry"},
    {"question":"What’s the term for an oasis-dwelling nomadic group?",
     "answer":"bedouin"},
    {"question":"What kind of reptile often lives in deserts?",
     "answer":"lizard"},
]

#VARIABLES 

total_score = 0
lose_count = 0 
inventory = []
pet_name = ""
endings = []
dialog_box_visible = False
game_state = "dialog"
dialog_time = pygame.time.get_ticks()
desert_weather = random.choice(weather)
intro_started = False
right_choice = ""
left_choice = ""
right_choice_pos = (80, 600)
left_choice_pos = (780, 600)
selected_choice = ""
choice_character_visible = False
cactus_width = 10
cactus_height = 17
cactus_visible = False
cactus_1st_dialog_started = False
intro_done = False
cactus_1st_dialog_done = False
cactus_questions_started = False

#DIALOG
intro = ["You find yourself in the middle of the desert.",
        "You don’t remember how you got here. Your head is foggy,"
        f"and the weather is {desert_weather}.",
        "You’re thirsty.",
        "Hungry.",
        "Dizzy.",
        "The sand stretches endlessly in every direction.",
        "You hear a strange sound, you look and"
        " " "spot a grinning floating cactus.",
        "Yes, it has a face.",
        "You don't know if it is just dehydration"
        " " "or that you have lost your mind"]

cactus_1st_dialog = ["Hi there! Do you want to play"
                      " " "a small trivia game? :D",
                      "3 trivia questions,"
                      " " "if you get 1 right you will earn 5 points!"
                      " " "That is a great way to increase your total score!",
                      "fun right? :D"]

cactus_happy = ["You agree to the floating cactus offer" 
                " " ", it grins widely and askes:"]

cactus_sad = ["You refuse as a normal sane human being.",
              "it poutes and says 'fine! I will"
              " " "be back!' then it vanishes."]
current_dialog = intro
current_index = 0

#IMAGES
bg1 = pygame.image.load("Images/bg1.jpg").convert_alpha()
dialog_box = pygame.image.load("Images/dialog_box.png").convert_alpha()
dialog_ch = pygame.image.load("Images/dialog_ch_symbol.png").convert_alpha()
choice_character = pygame.image.load("Images/choice_character.png").convert_alpha()
dialog_cactus = pygame.image.load("Images/dialog_cactus_symbol.png").convert_alpha()
cactus_normal = pygame.image.load("Images/cactus_character.png").convert_alpha()
cactus_angry = pygame.image.load("Images/cactus_angry.png").convert_alpha()

cactus = cactus_normal
dialog_character = dialog_ch

#FONT
font = pygame.font.Font("fonts/messages.ttf", 35)

#FUNCTIONS

def draw_message(message, x, y):
    text_surface = font.render(message, True, (0, 0, 0))
    screen.blit(text_surface, (x, y))

def timer_reset():
    global dialog_time
    dialog_time = pygame.time.get_ticks()

def text(message, width, x, y):
    current_line = ""
    lines = []
    test_line = ""
    words = message.split()
    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] < width: 
            current_line = test_line
        else:
            lines.append(current_line )
            current_line = word + " "
    lines.append(current_line)
    for line in lines:
        draw_message(line, x, y)
        y = y + 5 + font.size("a")[1]

def dialog_check():
    if dialog_box_visible:
        screen.blit(dialog_box, (51, 487))
        screen.blit(dialog_character,(103, 514))
        text(current_dialog[current_index], 1040, 185, 514)

def choices(left_choice, right_choice):
    global choice_character_visible
    if dialog_box_visible:
        screen.blit(dialog_box, (51, 487))
        if selected_choice == "left_choice":
            screen.blit(choice_character, (100, 600))
        elif selected_choice == "right_choice":
            screen.blit(choice_character, (800, 600))
        else:
            screen.blit(choice_character, (390, 600))
        choice_character_visible = True
        text(left_choice, 550, 80, 550)
        text(right_choice, 550, 780, 550)


def start():
    screen.blit(bg1, (0, 0))

def cactus_questions(comment, cactus_last_line):
    choices("Agree to play", "Cancel the offer")




while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            print(f"Key pressed: {event.key}")
            if event.key == pygame.K_F11: 
                pygame.display.toggle_fullscreen()

            if event.key == pygame.K_z: 
                if dialog_box_visible and game_state == "dialog":
                    if current_index < len(current_dialog) - 1:
                        current_index += 1
                    else:
                        dialog_box_visible = False

                elif dialog_box_visible and game_state == "choice_cactus_1":
                    if selected_choice == "right_choice":
                        game_state = "dialog"
                        current_dialog = cactus_sad
                        cactus = cactus_angry
                        current_index = 0
                        dialog_box_visible = True
                    elif selected_choice == "left_choice":
                        game_state = "dialog"
                        current_dialog = cactus_happy
                        current_index = 0
                        dialog_box_visible = True

            if event.key == pygame.K_RIGHT:
                if choice_character_visible:
                    selected_choice = "right_choice"

            if event.key == pygame.K_LEFT:
                if choice_character_visible:
                    selected_choice = "left_choice"


        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)
    
    start()
    current_time = pygame.time.get_ticks()

    if current_time - dialog_time > 3000 and not intro_started:
        dialog_box_visible = True
        intro_started = True
    

    if current_dialog == intro:
        if current_index >= 6:
            cactus_visible = True
        if current_index == len(current_dialog) - 1:
            intro_done = True
    if cactus_visible:
        if cactus_width < 300:
            cactus_width += 1
            cactus_height += 1.67

    scaled_cactus = pygame.transform.scale(cactus, (int(cactus_width), int(cactus_height)))
    x = (WIDTH - int(cactus_width)) // 2
    y = 487 - int(cactus_height) + math.sin(pygame.time.get_ticks() / 500) * 10
    if cactus_visible:
        screen.blit(scaled_cactus, (x, y))
    if not cactus_1st_dialog_started and intro_done:
        dialog_box_visible = True
        cactus_1st_dialog_started = True
        current_dialog = cactus_1st_dialog
        dialog_character = dialog_cactus
        current_index = 0

    if current_dialog == cactus_1st_dialog:
        if current_index == len(current_dialog) - 1 and not cactus_questions_started:
            cactus_1st_dialog_done = True
            game_state = "choice_cactus_1"
            cactus_questions_started = True

    if current_dialog == cactus_sad:
        if current_index == len(current_dialog) - 1:
            cactus_visible = False

            

    
    if game_state == "dialog":
        dialog_check()
    elif game_state == "choice_cactus_1":
        cactus_questions("That was weird", "That was soooo much fun!")


    pygame.display.update()
