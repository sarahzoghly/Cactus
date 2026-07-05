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
     "answer":"chalk", "wrong":["marker pen", "crayons", "pencil"]},
    {"question":"What's the name of the organ that helps you breathe?",
     "answer":"lungs", "wrong":["kidney", "langs", "toes"]},
    {"question":"What's the colored part of your eye called?",
     "answer":"iris", "wrong":["cornea", "pupil", "retina"]},
    {"question":"What do you call a house made of ice?",
     "answer":"igloo", "wrong":["ice-house", "housed-ice", "iqloo"]},
    {"question":"What is the hardest natural substance on Earth?",
     "answer":"diamond", "wrong":["iron", "copper", "uranium"]},
    {"question":"What planet is known for its rings?",
     "answer":"saturn", "wrong":["uranus", "neptune", "pluto"]},
    {"question":"What is H2O more commonly known as?",
     "answer":"water", "wrong":["air", "oxygen", "hydrocloric acid"]},
    {"question":"What do we call molten rock upon the surface after it erupts from a volcano?",
     "answer":"lava", "wrong":["magma", "igneous rock", "nagma"]},
    {"question":"What part of the body pumps blood?",
     "answer":"heart", "wrong":["liver", "spleen", "red blood cells"]},
    {"question":"What tool tells you which direction is north?",
     "answer":"compass", "wrong":["clock", "map", "tracking device"]},
    {"question":"In a website browser address bar, what does 'www' stand for?",
     "answer":"world wide web", "wrong":["we wove websites <3", "wide world web", "web world wide"]},
    {"question":"In what year was the Internet opened to the public?",
     "answer":"1993", "wrong":["1994", "1899", "1983"]},
    {"question":"What's the largest animal on Earth?",
     "answer":"blue whale", "wrong":["white whale", "dolphin", "elephant"]},
    {"question":"What is the largest desert on Earth?",
     "answer":"antarctica", "wrong":["sahara", "shara", "the arctic desert"]},
    {"question":"What color do you get if you mix red and yellow?",
     "answer":"orange", "wrong":["blue", "black", "purple"]},
    {"question":"What do cows drink?",
     "answer":"water", "wrong":["milk", "orange juice", "grass"]},
    {"question":"What season comes after winter?",
     "answer":"spring", "wrong":["summer", "winter", "autumn"]},
    {"question":"What has hands but no arms or legs?",
     "answer":"clock", "wrong":["gloves", "pans", "chairs"]},
    {"question":"What plant is famous for surviving in deserts?",
     "answer":"cactus", "wrong":["floating cactus", "grass", "roses"]},
    {"question":"What animal is known as the 'ship of the desert'?",
     "answer":"camel", "wrong":["lizard", "snake", "tiger"]},
    {"question":"What's the main gas in the air we breathe?",
     "answer":"nitrogen", "wrong":["oxygen", "carbon dioxide", "hydrogen"]},
    {"question":"What's the name of the red planet?",
     "answer":"mars", "wrong":["mercury", "venus", "earth"]},
    {"question":"What is full of holes but still holds water?",
     "answer":"sponge", "wrong":["strainer", "colander", "cup"]},
    {"question":"What's something you break before you use it?",
     "answer":"egg", "wrong":["pencil", "knife", "microwave"]},
    {"question":"What language do people speak in Brazil?",
     "answer":"portuguese", "wrong":["brazilian", "english", "spanish"]},
    {"question":"What fruit has its seeds on the outside?",
     "answer":"strawberry", "wrong":["tomatoes", "peaches", "raspberries"]},
    {"question":"What's the term for an oasis-dwelling nomadic group?",
     "answer":"bedouins", "wrong":["arabs", "beduoins", "oasisens"]},
    {"question":"What kind of reptile often lives in deserts?",
     "answer":"lizard", "wrong":["snakes", "salamanders", "ostriches"]},
]
#VARIABLES 

total_score = 0
round_score = 0
lose_count = 0 
inventory_items = []
inventory_visible = True
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

trivia_active = False
trivia_question_num = 0
current_question = None
option_positions = {}
correct_position = ""
trivia_showing_result = False
trivia_done = False
trivia_selected = "A"

result_timer = 0
showing_trivia_result = False

cactus_bonus = False

cactus_last_line = ""
narrator_last_line =""
lines = ["That was soooo much fun!", "Till next time!", "Fun, right?", "Bye!"]
narrator_lines = ["That was weird.", "You are planning to play again next time, aren't you?", "Well, that is your life now."]

cactus_line_done = False
narrator_line_done = False
score_line_done = False

bucket_taken = False 
bucket_scene_started = False
bucket_choice_started = False

trivia_dialog = []

bucket_timer = 0 
bucket_scene_started = False

jeep_man_visible = False
trivia_round = 1

man_back_timer = 0
man_back = False
man_back_bonus = False

post_trivia_1_done = False 

strange_sound = random.choice(sound)

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
              "fine! I will"
              " " "be back!",
              "That was weird."]
bucket_dialog = ["You looked around and there was an empty bucket.",
                 "You remembered something about having to fill it.", 
                 "nothing"]
jeep_vs_pond = ["In the distance, you spot two things:",
               "-A shimmering water pond far to your left.",
               "-A black jeep, strange and unmoving, off to the right.",
               "You have to choose. You can’t just sit here"
                " " "and wait for the sun to finish you off.",
                "nothing"]
jeep_vs_pond_main = [] 
jeep_dialog = ["You walk toward the jeep.",
               "When you reach it, you see a man inspecting the engine.",
               "It looks like the jeep is broken.",
               "nothing"]
pond_dialog = ["You start walking toward the water pond.",
               "But with every step, the distance"
                " " "seems to stretch farther away.",
                "You keep walking... and walking...",
                "nothing"]
pond_back_dialog = ["You lost 5 points for coming herefrom the start!",
                    "You went back to where you were."] + jeep_vs_pond
cactus_rare_dialog = ["You heard a strange sound", 
                      "as you looked, it turned out to be the"
                       " " "floating cactus again..",
                       "Hi there!",
                       "What are you doing here? As far"
                        " " "as I know, this place is empty.",
                        "Do you want a drive to the jeep?"
                        " " "there is a guy there that may help you!",
                        "nothing"]
#EDITING
cactus_rare_happy = ["It holds you happily,and flies away with you humming.",
                     "you arrive in a couple of minutes.",
                     "Here you go!' it said happily.",
                     "Also, here is 20 points! They may help"
                     " " "you :D' it said before vanishing",
                     f"Your total score now is {total_score}.",
                     "Well, it turned out to be helpful.",
                     "nothing"]
cactus_rare_sad = ["fine! I shouldn't have offered you help from the start",
                   "It vanished looking upset.",
                   "It is your fault.",
                   "You continue walking."
                   "And walking",
                   "The pond never gets any closer.",
                   "It was a mirage.",
                   "You're more lost than before,"
                    " " "the heat pressing down"
                    " " "on you like a weight.",
                    "Exhausted, dizzy, and drained"
                    " " "from the endless walk",
                    "You collapse in the sand."]
mirage_dialog = ["The pond never gets any closer.",
                 "It was a mirage.",
                 "You're more lost than before,"
                 " " "the heat pressing down on you like a weight.",
                 "Exhausted, dizzy, and"
                 " " "drained from the endless walk",
                 "You collapse in the sand."]

jeep_back_dialog = []

jeep_man_talk = ["You call for him and he walks toward you with a questioning look",
                 "You explain that you're lost and don’t remember how you got here.",
                "I was headed to a nearby village, but the jeep broke down.",
                 "The jeep needs water to start again",
                 "There is a well nearby but I have nothing to fetch water with.",
                 "If you help him he might help you in return.",
                 "nothing"]

bucket_given_dialog = ["You hand him the bucket",
                       "He takes it, walks off toward the well.",
                       "As you wait you hear a strange sound, when you looked up you spot it again.",
                       "The Floating Cactus.",
                       "Hey there again!",
                       "Do you want to play another trivia game?",
                       "Just like the last time you earn 5 points for each correct question and lose 5 for each wrong one!",
                       "Remember that can easily increase your score if you are smart enough!",
                       "nothing"]

bucket_thrown_dialog= ["You threw the bucket directly at his head.",
                        "OW! What is wrong with you!?",
                        "You lost the bucket.",
                        "You know what? I am taking this and leaving you.",
                        "You called after him.",
                        "What?",
                        "You offered to help him. He sighed deeply.",
                        "Fine. Come make yourself useful",
                        "You were just going after him but a strange sound stopped you.",
                        "You looked up.",
                        "It was The Floating Cactus.",
                        "Hey there again!",
                        "Do you want to play another trivia game?",
                        "Just like the last time you earn 5 points for each correct question and lose 5 for each wrong one!",
                        "Remember that can easily increase your score if you are smart enough!",
                        "nothing"]

man_back_dialog = ["The man comes back with the bucket full of water",
                  "He walks to the jeep.",
                  "After pouring the water into the engine, he fiddles with it for a while"
                   " " "and the jeep starts.",
                   "You have earned 10 points for choosing right!",
                   f"Your total score now is {total_score} points!",
                   "Get in",
                   "You hop into the jeep",
                   "As soon as he began driving, your eyes closed. Heavy with sleep.",
                   "...",
                   "...",
                   "...",
                   "You opened your eyes and you were at the entrance of a village.",
                   "Here we are",
                   "I've got some business to take care of. I have to go. See you around.",
                   "nothing"]
stare_man_dialog = ["You stared at him.",
                    "...",
                    "...",
                    "Stop looking at me like that",
                    "...",
                    "Stop.",
                    "Ok. Ok. Just.. come help me, let's find a way to make it work.",
                    "nothing"]
help_dialog = ["You offered to help",
               "I told you. I need something to fetch the water with.",
               "You offered your shoe.",
               "Are you serious?",
               "You nodded. He sighed",
               "That will take forever. Just come help me, let's find a way to make it work.",
               "nothing"]

man_die = ["You both try everything to fix" #BACK
            " " "the jeep, but nothing works.",
            "You're too hungry to think straight.",
            "The man crawls into the jeep.",
            "He looks exhausted—maybe he"
            " " "passed out, maybe worse.",
            "You hear a strange sound in the distance"
            " " f"—{strange_sound}, you think.",
            "It doesn't look safe to stay here.",
            "Night falls.",
            "You lie on the sand, eyes"
            " " "heavy, body aching.",
            "The stars blur.",
            "Everything fades.",
            "You don’t hear anything anymore.",
            "You had to get the bucket."]
current_dialog = intro
current_index = 0
#ENDINGS
collapse = False
points_poor = False

#IMAGES
inventory_bg = pygame.image.load("Images/inventory.png").convert_alpha()

bg1 = pygame.image.load("Images/bg1.jpg").convert_alpha()
dialog_box = pygame.image.load("Images/dialog_box.png").convert_alpha()
dialog_ch = pygame.image.load("Images/dialog_ch_symbol.png").convert_alpha()
choice_character = pygame.image.load("Images/choice_character.png").convert_alpha()
dialog_cactus = pygame.image.load("Images/dialog_cactus_symbol.png").convert_alpha()
dialog_man = pygame.image.load("Images/dialog_man_symbol.png").convert_alpha()
cactus_normal = pygame.image.load("Images/cactus_character.png").convert_alpha()
cactus_angry = pygame.image.load("Images/cactus_angry.png").convert_alpha()
cactus_points_won = pygame.image.load("Images/cactus_points_won.png").convert_alpha()
cactus_points_loss = pygame.image.load("Images/cactus_points_loss.png").convert_alpha()
cactus = cactus_normal
dialog_character = dialog_ch
bg2 = pygame.image.load("Images/bg2.jpg").convert_alpha()
bg_pond = pygame.image.load("Images/bg_pond.jpg").convert_alpha()
bg_jeep = pygame.image.load("Images/bg_jeep.jpg").convert_alpha()
bucket_img = pygame.image.load("Images/bucket.png").convert_alpha()
bucket_icon = pygame.transform.scale(bucket_img, (60, 60))
bg_flying = pygame.image.load("Images/bg_flying.jpg").convert_alpha()
bg_walking_1 = pygame.image.load("Images/bg_walking_1.jpg").convert_alpha()
bg_walking_2 = pygame.image.load("Images/bg_walking_2.jpg").convert_alpha()
bg_walking_3 = pygame.image.load("Images/bg_walking_3.jpg").convert_alpha()
bg_collapse = pygame.image.load("Images/bg_collapse.jpg").convert_alpha()
jeep_man_normal = pygame.image.load("Images/jeep_man_normal.png").convert_alpha()
bg_jeep_man_inspecting = pygame.image.load("Images/bg_jeep_man_inspecting.jpg").convert_alpha()
jeep_man_angry = pygame.image.load("Images/jeep_man_angry.png").convert_alpha()
jeep_man_bucket = pygame.image.load("Images/jeep_man_bucket.png").convert_alpha()
bg_in_jeep = pygame.image.load("Images/bg_in_jeep.jpg").convert_alpha()
bg_jeep_night_1 = pygame.image.load("Images/bg_jeep_night_half.jpg").convert_alpha()
bg_jeep_night_2 = pygame.image.load("Images/bg_jeep_night_half2.jpg").convert_alpha()
bg_jeep_night_3 = pygame.image.load("Images/bg_jeep_night_full.jpg").convert_alpha()
bg_stars = pygame.image.load("Images/bg_stars.jpg").convert_alpha()
bg_stars_blur = pygame.image.load("Images/bg_stars_blur.jpg").convert_alpha()
bg_village_entrance = pygame.image.load("Images/bg_village_entrance.jpg").convert_alpha()

#SLOTS
slot1 = pygame.image.load("Images/slot1.png").convert_alpha()
slot2 = pygame.image.load("Images/slot2.png").convert_alpha()
slot3 = pygame.image.load("Images/slot3.png").convert_alpha()
slot4 = pygame.image.load("Images/slot4.png").convert_alpha()
slot5 = pygame.image.load("Images/slot5.png").convert_alpha()
#RECTS
slot1_rect = slot1.get_rect(topleft=(420, 10))
slot2_rect = slot2.get_rect(topleft=(510, 10))
slot3_rect = slot3.get_rect(topleft=(600, 10))
slot4_rect = slot4.get_rect(topleft=(690, 10))
slot5_rect = slot5.get_rect(topleft=(780, 10))

current_bg = bg1
jeep_man = jeep_man_normal

#FONT
font = pygame.font.Font("fonts/messages.ttf", 30)

#FUNCTIONS
def check_score():
    global game_state, dialog_box_visible, current_dialog, current_index, points_poor, trivia_active
    if total_score < 0:
        current_dialog = ["You have less than 0 points! Sorry, that means game over for you!"]
        dialog_box_visible = True
        current_index = 0
        trivia_active = False
        if not points_poor:
            points_poor = True
        game_state = "game_over"

def draw_inventory():
    screen.blit(inventory_bg, (0, 0))
    
    screen.blit(slot1, slot1_rect.topleft)
    screen.blit(slot2, slot2_rect.topleft)
    screen.blit(slot3, slot3_rect.topleft)
    screen.blit(slot4, slot4_rect.topleft)
    screen.blit(slot5, slot5_rect.topleft)

    draw_inventory_items()

def inventory_add(found_thing):
    inventory_items.append(found_thing)

def draw_inventory_items():

    if len(inventory_items) > 0:
        item_rect = inventory_items[0].get_rect(center=slot1_rect.center)
        screen.blit(inventory_items[0], item_rect)

    if len(inventory_items) > 1:
        item_rect = inventory_items[1].get_rect(center=slot2_rect.center)
        screen.blit(inventory_items[1], item_rect)
    
    if len(inventory_items) > 2:
        item_rect = inventory_items[2].get_rect(center=slot3_rect.center)
        screen.blit(inventory_items[2], item_rect)

    if len(inventory_items) > 3:
        item_rect = inventory_items[3].get_rect(center=slot4_rect.center)
        screen.blit(inventory_items[3], item_rect)

    if len(inventory_items) > 4:
        item_rect = inventory_items[4].get_rect(center=slot5_rect.center)
        screen.blit(inventory_items[4], item_rect)

def restart():
    global total_score, round_score, lose_count, inventory_items, pet_name
    global dialog_box_visible, game_state, dialog_time, intro_started
    global selected_choice, choice_character_visible
    global cactus_width, cactus_height, cactus_visible
    global cactus_1st_dialog_started, intro_done, cactus_1st_dialog_done, cactus_questions_started
    global trivia_active, trivia_question_num, current_question, option_positions
    global correct_position, trivia_done, trivia_selected, result_timer, showing_trivia_result
    global cactus_last_line, narrator_last_line, cactus_line_done, narrator_line_done, score_line_done
    global current_dialog, current_index, cactus, dialog_character
    global bucket_taken, bucket_scene_started, bucket_choice_started, bucket_timer
    global current_bg
    global collapse, points_poor, cactus_points, jeep_man_visible
    global jeep_vs_pond_main, jeep_man
    global trivia_round, man_back, man_back_timer, man_back_bonus
    global cactus_bonus, trivia_showing_result, post_trivia_1_done


    post_trivia_1_done = False 
    total_score = 0
    round_score = 0
    lose_count = 0
    inventory_items = []
    pet_name = ""
    dialog_box_visible = False
    game_state = "dialog"
    dialog_time = pygame.time.get_ticks()
    intro_started = False
    selected_choice = ""
    choice_character_visible = False
    cactus_width = 10
    cactus_height = 17
    cactus_visible = False
    cactus_1st_dialog_started = False
    intro_done = False
    cactus_1st_dialog_done = False
    cactus_questions_started = False
    trivia_active = False
    trivia_question_num = 0
    current_question = None
    option_positions = {}
    correct_position = ""
    trivia_done = False
    trivia_selected = "A"
    result_timer = 0
    showing_trivia_result = False
    cactus_last_line = ""
    narrator_last_line = ""
    cactus_line_done = False
    narrator_line_done = False
    score_line_done = False
    current_dialog = intro
    current_index = 0
    current_bg = bg1
    cactus = cactus_normal
    dialog_character = dialog_ch
    bucket_taken = False
    bucket_scene_started = False
    bucket_choice_started = False
    bucket_timer = 0
    bucket_scene_started = False
    man_back_bonus = False
    collapse = False
    points_poor = False
    cactus_points = False
    jeep_man_visible = False
    trivia_round = 1
    man_back = False
    man_back_timer = 0
    man_back_bonus = False  
    cactus_bonus = False    
    trivia_showing_result = False
    trivia_dialog = []
    jeep_man = jeep_man_normal
    jeep_vs_pond_main = []  

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
        if jeep_man_visible: #EDIT
            screen.blit(jeep_man, (480, 280))
            screen.blit(dialog_box, (51, 487))
            screen.blit(dialog_character,(103, 514))
            text(current_dialog[current_index], 1040, 185, 514)
        else:
            screen.blit(dialog_box, (51, 487))
            screen.blit(dialog_character,(103, 514))
            text(current_dialog[current_index], 1040, 185, 514)

def choices(left_choice, right_choice):
    global choice_character_visible
    if dialog_box_visible:
        screen.blit(dialog_box, (51, 487))
        if selected_choice == "left_choice":
            screen.blit(choice_character, (200, 560))
        elif selected_choice == "right_choice":
            screen.blit(choice_character, (970, 560))
        else:
            screen.blit(choice_character, (590, 560))
        choice_character_visible = True
        text(left_choice, 550, 100, 560)
        text(right_choice, 514, 820, 560)


def start():
    screen.blit(current_bg, (0, 0))

def cactus_questions(comment, cactus_last_line):
    choices("Agree to play", "Cancel the offer")

def trivia_question_setup():
    global option_positions
    global correct_position
    global current_question
    the_trivia_q = random.choice(trivia_questions)
    current_question = the_trivia_q
    wrong_answers = the_trivia_q["wrong"]
    right_answer = the_trivia_q["answer"]
    answers = []
    answers.append(right_answer)
    answers = answers + wrong_answers
    random.shuffle(answers)
    option_positions = {"A":answers[0], "B":answers[1], "C":answers[2], "D":answers[3]}
    
    for position, answer in option_positions.items():
        if answer == right_answer:
            correct_position = position


def draw_trivia():
    if trivia_active:
        screen.blit(dialog_box, (51, 487))
        text(current_question["question"], 1090, 80, 510)
        text(option_positions["A"], 500, 90, 565)
        text(option_positions["B"], 500, 925, 565)
        text(option_positions["C"], 500, 90, 620)
        text(option_positions["D"], 500, 925, 620)

        if trivia_selected == "B":
            screen.blit(choice_character, (880, 565))
        elif trivia_selected == "C":
            screen.blit(choice_character, (60, 620))   
        elif trivia_selected == "D":
            screen.blit(choice_character, (880, 620))
        else:
            screen.blit(choice_character, (60, 565))

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11: 
                pygame.display.toggle_fullscreen()

        

            if event.key == pygame.K_z: 
                if dialog_box_visible and game_state == "dialog":
                    if current_index < len(current_dialog) - 1:
                        current_index += 1
                    else:
                        dialog_box_visible = False

                if game_state == "game_over":
                    if current_index < len(current_dialog) - 1:
                        current_index += 1
                    else:
                        restart()        

                elif dialog_box_visible and game_state == "choice_cactus_1":
                    if selected_choice == "right_choice":
                        game_state = "dialog"
                        current_dialog = cactus_sad
                        cactus = cactus_angry
                        current_index = 0
                        dialog_box_visible = True
                    elif selected_choice == "left_choice":
                        game_state = "dialog"
                        trivia_active = True
                        trivia_question_num = 0
                        round_score = 0
                        trivia_question_setup()
                        current_index = 0
                        dialog_box_visible = False

                
                

                elif trivia_active:
                    if trivia_selected == correct_position:
                        cactus = cactus_points_won
                        total_score += 5
                        round_score += 5
                        trivia_question_num += 1

                        if trivia_question_num >= 3:
                            trivia_done = True
                            trivia_active = False
                            cactus_last_line = random.choice(lines)
                            narrator_last_line = random.choice(narrator_lines)
                            score_line = f"You got {round_score} points. Your total score is {total_score}!"
                            showing_trivia_result = True
                            dialog_box_visible = False
                            result_timer = pygame.time.get_ticks()
                            
                        else:
                            trivia_question_setup()
                    elif trivia_selected != correct_position:
                        cactus = cactus_points_loss
                        total_score -= 5
                        round_score -= 5
                        trivia_question_num += 1
                        check_score()
                        if total_score >= 0:
                            if trivia_question_num >= 3:
                                trivia_done = True
                                trivia_active = False
                                lines = ["That was soooo much fun!", "Till next time!", "Fun, right?", "Bye!"]
                                narrator_lines = ["That was weird.", "What was that?", "Well, that is your life now."]
                                cactus_last_line = random.choice(lines)
                                narrator_last_line = random.choice(narrator_lines)
                                score_line = f"You got {round_score} points. Your total score is {total_score}!"
                                showing_trivia_result = True
                                dialog_box_visible = False
                                result_timer = pygame.time.get_ticks()
                            else:
                                trivia_question_setup()     

                elif game_state == "bucket_choice":
                    if selected_choice == "right_choice":
                        game_state = "dialog"
                        jeep_vs_pond_main = ["You left the bucket"] + jeep_vs_pond
                        current_dialog = jeep_vs_pond_main
                        current_index = 0
                        dialog_box_visible = True
                    elif selected_choice == "left_choice":
                        game_state = "dialog"
                        inventory_add(bucket_icon)
                        bucket_taken = True
                        
                        jeep_vs_pond_main = ["You took the bucket"] + jeep_vs_pond
                        current_dialog = jeep_vs_pond_main
                        current_index = 0
                        dialog_box_visible = True

                elif game_state == "jeep_vs_pond_choice":
                    if selected_choice == "right_choice":
                        game_state = "dialog"
                        current_dialog = jeep_dialog
                        current_bg = bg_jeep
                        current_index = 0
                        dialog_box_visible = True
                    elif selected_choice == "left_choice":
                        game_state = "dialog"
                        current_dialog = pond_dialog
                        current_bg = bg_pond
                        current_index = 0
                        dialog_box_visible = True
  
                elif game_state == "pond_choices":
                    if selected_choice == "right_choice":
                        total_score -= 5
                        check_score()
                        if total_score >= 0:
                            current_dialog = pond_back_dialog
                            game_state = "dialog"
                            current_index = 0
                            dialog_box_visible = True
                    elif selected_choice == "left_choice":
                        rare_event_mirage = 0 #random.randint(1, 15) EDIT LATER 
                        if rare_event_mirage == 1:
                            current_dialog = cactus_rare_dialog
                            game_state = "dialog"
                            current_index = 0
                            dialog_box_visible = True
                        else:
                            current_dialog = mirage_dialog
                            game_state = "dialog"
                            current_index = 0
                            dialog_box_visible = True

                    
                        
                        

                elif game_state == "cactus_rare_choices":
                    if selected_choice == "right_choice":
                        current_dialog = cactus_rare_sad
                        game_state = "dialog"
                        current_index = 0
                        dialog_box_visible = True
                    elif selected_choice == "left_choice":
                        current_dialog = cactus_rare_happy
                        game_state = "dialog"
                        current_index = 0
                        dialog_box_visible = True

                elif game_state == "jeep_choices": 
                    if selected_choice == "right_choice":
                        total_score -= 5
                        check_score()
                        if total_score >= 0:
                            jeep_back_dialog = ["You lost 5 points for changing your choice!", f"Your score now is {total_score}.", "nothing"] 
                            game_state = "dialog"
                            current_dialog = jeep_back_dialog
                            current_index = 0
                            dialog_box_visible = True
                    elif selected_choice == "left_choice":
                        current_dialog = jeep_man_talk
                        game_state = "dialog"
                        current_index = 0
                        dialog_box_visible = True    
#HERE
                elif game_state == "jeep_bucket_choices":
                    if selected_choice == "left_choice":
                        current_dialog = bucket_given_dialog
                        inventory_items.remove(bucket_icon)
                        game_state = "dialog"
                        current_index = 0
                        dialog_box_visible = True
                    elif selected_choice == "right_choice":
                        total_score -= 5
                        check_score()
                        if total_score >= 0:
                            current_dialog = bucket_thrown_dialog
                            inventory_items.remove(bucket_icon)
                            game_state = "dialog"
                            current_index = 0
                            dialog_box_visible = True

                elif dialog_box_visible and game_state == "trivia_game_2":
                    if selected_choice == "left_choice":
                        trivia_round = 2
                        trivia_active = True
                        trivia_question_num = 0
                        round_score = 0
                        trivia_question_setup()
                        game_state = "dialog"
                        dialog_box_visible = False
                    elif selected_choice == "right_choice":
                        cactus = cactus_angry
                        current_dialog = ["You refuse.",
                                          "Fine! FINE. I won't help you next time!",
                                          "It vanishes looking deeply offended."]
                        current_index = 0
                        dialog_box_visible = True
                        game_state = "dialog"
                        man_back = True
                        man_back_timer = pygame.time.get_ticks()
                        bucket_scene_started = False  

                elif game_state == "jeep_no_bucket_choices":
                    if selected_choice == "right_choice":
                        current_dialog = stare_man_dialog
                        game_state = "dialog"
                        current_index = 0
                        dialog_box_visible = True
                    elif selected_choice == "left_choice":
                        current_dialog = help_dialog
                        game_state = "dialog"
                        current_index = 0
                        dialog_box_visible = True

            if event.key == pygame.K_RIGHT:
                if choice_character_visible:
                    selected_choice = "right_choice"
                if trivia_active:
                    if trivia_selected == "A":
                        trivia_selected = "B"
                    elif trivia_selected == "B":
                        trivia_selected = "C"
                    elif trivia_selected == "C":
                        trivia_selected = "D"
                        
                       

            if event.key == pygame.K_LEFT:
                if choice_character_visible:
                    selected_choice = "left_choice"
                if trivia_active:
                        if trivia_selected == "B":
                            trivia_selected = "A"
                        elif trivia_selected == "C":
                            trivia_selected = "B"
                        elif trivia_selected == "D":
                            trivia_selected = "C"


        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
    
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
            cactus = cactus_normal
            dialog_character = dialog_ch
            if not dialog_box_visible and not bucket_scene_started:
                bucket_timer = pygame.time.get_ticks()
                bucket_scene_started = True
            if current_index == 1:
                dialog_character = dialog_cactus
            if current_index == 2:
                dialog_character = dialog_ch
    
    if current_dialog == trivia_dialog:
        if current_index == 2:
            cactus_visible = False
            dialog_character = dialog_ch
        if trivia_round == 1:
            if current_index == len(trivia_dialog) - 1 and not dialog_box_visible and not post_trivia_1_done:
                post_trivia_1_done = True
                bucket_timer = pygame.time.get_ticks()
                bucket_scene_started = True
            #TRIVIA ROUND 2
        elif trivia_round == 2:
            if current_index == len(trivia_dialog) - 1 and not dialog_box_visible and not man_back:
                man_back = True
                man_back_timer = pygame.time.get_ticks()
                bucket_scene_started = False

    if current_dialog == bucket_dialog:
        if current_index == 1:
            current_bg = bg2 
        if current_index == len(current_dialog) - 1:
            game_state = "bucket_choice"

    if current_dialog == jeep_vs_pond_main:
        if current_index == 0 or current_index == 1:
            current_bg = bg2
        elif current_index == 2:
            current_bg = bg_pond
        elif current_index == 3:
            current_bg = bg_jeep
        elif current_index == 4:
            current_bg = bg2

        if current_index == len(current_dialog) - 1:
            game_state = "jeep_vs_pond_choice"
    
    
    if current_dialog == pond_dialog:
        if current_index == 3:
            game_state = "pond_choices"
    
    if current_dialog == pond_back_dialog:
        if current_index == 2:
            current_bg = bg2
        if current_index == len(current_dialog) - 1:
            game_state = "jeep_vs_pond_choice"

    if current_dialog == cactus_rare_dialog:
        if current_index == 1:
            cactus_visible = True
        if current_index == 2:
            dialog_character = dialog_cactus
        if current_index == len(current_dialog) - 1:
            game_state = "cactus_rare_choices"
            dialog_character = dialog_ch

    if current_dialog == cactus_rare_happy:
        cactus_visible = False
        if not cactus_points:
            total_score += 20
            cactus_points = True
            cactus_rare_happy[4] = f"Your total score now is {total_score}."
        if current_index == 0:
            current_bg = bg_flying
        if current_index == 1:
            current_bg = bg_jeep
        if current_index == 2:
            dialog_character = dialog_cactus
            cactus_visible = True
        if current_index == 3:
            cactus_visible = True
        if current_index == 5:
            cactus_visible = False
            dialog_character = dialog_ch
        if current_index == len(current_dialog) - 1:
            game_state = "jeep" #EDIT LATER

    if current_dialog == cactus_rare_sad:
        cactus = cactus_angry
        if current_index == 0:
            dialog_character = dialog_cactus
        if current_index == 1:
            dialog_character = dialog_ch
            cactus_visible = False
        if current_index == 3:
            current_bg = bg_walking_1
        if current_index == 4:
            current_bg = bg_walking_2
        if current_index == 5:
            current_bg = bg_walking_1
        if current_index == 6:
            current_bg = bg_collapse
        if current_index == 8:
            current_bg = bg_flying
        if current_index == len(current_dialog) - 1:
            if not collapse:
                collapse = True
            game_state = "game_over"

    if current_dialog == mirage_dialog:
        if current_index == 0:
            current_bg = bg_walking_2
        if current_index == 1:
            current_bg = bg_walking_3
        if current_index == 2:
            current_bg = bg_collapse
        if current_index == len(current_dialog) - 1:
            if not collapse:
                collapse = True
            current_dialog = ["You collapsed in the desert heat... Game Over."]
            current_index = 0
            game_state = "game_over"

    if current_dialog == jeep_dialog:
        if current_index == 0:
            current_bg = bg_walking_3
        if current_index == 1:
            current_bg = bg_jeep_man_inspecting
        if current_index == len(current_dialog) - 1:
            game_state = "jeep_choices" 
        
    if current_dialog == jeep_back_dialog:
        if current_index == 1:
            current_bg = bg2
        if current_index == len(current_dialog) - 1:
            current_dialog = jeep_vs_pond_main
            current_index = 1  
            dialog_box_visible = True

    if current_dialog == jeep_man_talk:
        if current_index == 1:
            current_bg = bg_jeep
            jeep_man_visible = True
        if current_index == 2:
            dialog_character = dialog_man
        if current_index == 5:
            dialog_character = dialog_ch
        if current_index == len(current_dialog) - 1:
            if bucket_icon in inventory_items:
                game_state = "jeep_bucket_choices"
            else:
                game_state = "jeep_no_bucket_choices"

    elif current_dialog == bucket_given_dialog:
        if current_index == len(current_dialog) - 1:
            game_state = "trivia_game_2"
            dialog_box_visible = True
        if current_index == 0:
            if bucket_icon in inventory_items:
                inventory_items.remove(bucket_icon)
        if current_index == 1:
            jeep_man_visible = False
            current_bg = bg_jeep
        if current_index == 3:
            cactus_visible = True
        if current_index == 4:
            dialog_character = dialog_cactus

    elif current_dialog == bucket_thrown_dialog:
        if current_index == len(current_dialog) - 1:
            game_state = "trivia_game_2"
            dialog_box_visible = True
        if current_index == 0:
            if bucket_icon in inventory_items:
                inventory_items.remove(bucket_icon)
        if current_index == 1:
            jeep_man = jeep_man_angry
            dialog_character = dialog_man
        if current_index == 2:
            dialog_character = dialog_ch
        if current_index == 3:
            dialog_character = dialog_man
        if current_index == 4:
            dialog_character = dialog_ch
        if current_index == 5:
            dialog_character = dialog_man
        if current_index == 6:
            dialog_character = dialog_ch
        if current_index == 7:
            dialog_character = dialog_man
            jeep_man = jeep_man_normal
        if current_index == 8:
            dialog_character = dialog_ch
            jeep_man_visible = False
        if current_index == 10:
            cactus_visible = True
        if current_index == 11:
            dialog_character = dialog_cactus


        

    elif current_dialog == man_back_dialog:
        if current_index == 0:
            jeep_man = jeep_man_bucket
            jeep_man_visible = True
        if current_index == 1:
            jeep_man_visible = False
            current_bg = bg_jeep_man_inspecting
        if current_index == 3 and not man_back_bonus:
            man_back_bonus = True
            total_score += 10
            man_back_dialog[4] = f"Your total score now is {total_score}."
            check_score()
        if current_index == 5:
            jeep_man = jeep_man_normal
            jeep_man_visible = True
            dialog_character = dialog_man
            current_bg = bg_jeep
        if current_index == 6:
            dialog_character = dialog_ch
            jeep_man_visible = False
            current_bg = bg_in_jeep
        if current_index == 7:
            current_bg = bg_flying
        if current_index == 11:
            current_bg = bg_village_entrance
        if current_index == 12:
            dialog_character = dialog_man
        if current_index == len(current_dialog) - 1:
            #game_state
            dialog_box_visible = True
            man_back = False
        

    elif current_dialog == ["You refuse.", "Fine! FINE. I won't help you next time!", "It vanishes looking deeply offended."]:
        if current_index == 1:
            dialog_character = dialog_cactus
        if current_index == 2:
            dialog_character = dialog_ch
            cactus_visible = False
        if current_index == len(current_dialog) - 1:
            cactus = cactus_normal
        
    elif current_dialog == stare_man_dialog:
        if current_index == 3:
            dialog_character = dialog_man
        if current_index == 4:
            dialog_character = dialog_ch
        if current_index == 5:
            dialog_character = dialog_man
        if current_index == len(current_dialog) - 1:
            current_dialog = man_die
            current_index = 0

    elif current_dialog == help_dialog:
        if current_index == 1:
            dialog_character = dialog_man
        if current_index == 2:
            dialog_character = dialog_ch    
        if current_index == 3:
            dialog_character = dialog_man
        if current_index == 4:
            dialog_character = dialog_ch
        if current_index == 5:
            dialog_character = dialog_man
        if current_index == len(current_dialog) - 1:
            current_dialog = man_die
            current_index = 0
        
    elif current_dialog == man_die:
        if current_index == 0:
            jeep_man_visible = False
            current_bg = bg_jeep_man_inspecting
        if current_index == 2:
            current_bg = bg_jeep_night_1
        if current_index == 3:
            current_bg = bg_jeep_night_2
        if current_index == 6:
            current_bg = bg_jeep_night_3
        if current_index == 7:
            current_bg = bg_stars  
        if current_index == 8:
            current_bg = bg_stars_blur
        if current_index == 9:
            current_bg = bg_flying
        if current_index == len(current_dialog) - 1:
            collapse = True
            game_state = "game_over"
        
            
    #ENDINGS
    if collapse and "Collapsed on the hot sand" not in endings:
        endings.append("Collapsed on the hot sand")
    if points_poor and "Points Poor" not in endings:
        endings.append("Points Poor")   
        
        



        

            
    if current_bg == bg2:
        if not bucket_taken:
            screen.blit(bucket_img, (510,352))
        

    

    if bucket_scene_started and not dialog_box_visible:
        if current_time - bucket_timer > 2000:
            current_dialog = bucket_dialog
            current_index = 0
            dialog_box_visible = True

    if man_back and not dialog_box_visible:
        if current_time - man_back_timer > 2000:
            man_back_dialog[4] = f"Your total score now is {total_score} points!"  
            current_dialog = man_back_dialog
            current_index = 0
            dialog_box_visible = True


    if jeep_man_visible: #EDIT
            screen.blit(jeep_man, (480, 280))        

    
    if game_state == "dialog":
        dialog_check()
    elif game_state == "choice_cactus_1":
        cactus_questions("That was weird", "That was soooo much fun!") 
    elif game_state == "game_over":
        dialog_check() 

    elif game_state == "bucket_choice":
        choices("Take the bucket", "Leave the bucket")

    elif game_state == "jeep_vs_pond_choice":
        choices("Walk to the pond", "Walk to the jeep")

    elif game_state == "pond_choices":
        choices("Keep walking", "Go back")

    elif game_state == "cactus_rare_choices":
        choices("Accept the offer", "Refuse")

    elif game_state == "jeep_choices":
        choices("Talk to the man", "Go back")
#HERE
    elif game_state == "jeep_bucket_choices":
        choices("Give him the bucket", "Throw the bucket at his head.")

    elif game_state == "jeep_no_bucket_choices":
        choices("Try to help in another way", "Stare at him.")

    elif game_state == "trivia_game_2":
        choices("Let's play", "No. GO. AWAY.")

    if trivia_active:
        draw_trivia()

    if showing_trivia_result:
        if current_time - result_timer > 1000:
            cactus = cactus_normal
            showing_trivia_result = False
            game_state = "dialog"
            dialog_box_visible = True
            trivia_dialog = [score_line, cactus_last_line, narrator_last_line]
            current_dialog = trivia_dialog
            current_index = 0
            round_score = 0

    if inventory_visible:
        draw_inventory()    
            
    



    pygame.display.update()