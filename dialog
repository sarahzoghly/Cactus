import time 
import pygame
import random
import sys 

pygame.init()

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape Room")

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

#IMAGES
bg1 = pygame.image.load("Images/bg1.jpg").convert_alpha()
dialog_box = pygame.image.load("Images/dialog_box.png").convert_alpha()

#FONT
font = pygame.font.Font("fonts/messages.ttf", 25)

#DIALOG

start_1 = "You find yourself in the middle of the desert."

#FUNCTIONS
def dialog():
    if dialog_box_visible == True:
        screen.blit(dialog_box, (51, 487))

def draw_message(message, x, y):
    text_surface = font.render(message, True, (255, 255, 255))
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
        test_line = current_line + word
        if font.size(test_line)[0] < width:
            current_line = test_line
        else:
            lines.append(current_line )
            current_line = word + " "
    lines.append(current_line)
    for line in lines:
        draw_message(line, x, y)
        y = y + 5 + font.size("a")[1]

        



def start():
    screen.blit(bg1, (0, 0))





while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            print(f"Key pressed: {event.key}")
            if event.key == pygame.K_F11: 
                pygame.display.toggle_fullscreen()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)
    
    current_time = pygame.time.get_ticks()
    start()
    if current_time - dialog_time > 3000:
        dialog_box_visible = True
    if game_state == "dialog":
        dialog()
       

    pygame.display.update()

