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

cactus_last_line = ""
narrator_last_line =""
lines = ["That was soooo much fun!", "Till next time!", "Fun, right?", "Bye!"]
narrator_lines = ["That was weird.", "You are planning to play again next time, aren't you?", "Well, that is your life now."]

cactus_line_done = False
narrator_line_done = False
score_line_done = False

refused_bucket = False
bucket_scene_started = False
bucket_choice_started = False

trivia_dialog = []

bucket_timer = 0
bucket_scene_started = False

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
              " " "be back!' then it vanishes.",
              "That was weird."]
bucket_dialog = ["You looked around and there was an empty bucket.",
                 "You remembered something about having to fill it."]
current_dialog = intro
current_index = 0

#IMAGES
inventory_bg = pygame.image.load("Images/inventory.png").convert_alpha()

bg1 = pygame.image.load("Images/bg1.jpg").convert_alpha()
dialog_box = pygame.image.load("Images/dialog_box.png").convert_alpha()
dialog_ch = pygame.image.load("Images/dialog_ch_symbol.png").convert_alpha()
choice_character = pygame.image.load("Images/choice_character.png").convert_alpha()
dialog_cactus = pygame.image.load("Images/dialog_cactus_symbol.png").convert_alpha()
cactus_normal = pygame.image.load("Images/cactus_character.png").convert_alpha()
cactus_angry = pygame.image.load("Images/cactus_angry.png").convert_alpha()
cactus_points_won = pygame.image.load("Images/cactus_points_won.png").convert_alpha()
cactus_points_loss = pygame.image.load("Images/cactus_points_loss.png").convert_alpha()
cactus = cactus_normal
dialog_character = dialog_ch
bg2 = pygame.image.load("Images/bg2.jpg").convert_alpha()
bucket_img = pygame.image.load("Images/bucket.png").convert_alpha()

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

#FONT
font = pygame.font.Font("fonts/messages.ttf", 30)

#FUNCTIONS

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
    cactus = cactus_normal
    dialog_character = dialog_ch

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
            screen.blit(choice_character, (200, 560))
        elif selected_choice == "right_choice":
            screen.blit(choice_character, (970, 560))
        else:
            screen.blit(choice_character, (590, 560))
        choice_character_visible = True
        text(left_choice, 550, 100, 560)
        text(right_choice, 550, 820, 560)


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
            print(f"Key pressed: {event.key}")
            if event.key == pygame.K_F11: 
                pygame.display.toggle_fullscreen()

            if event.key == pygame.K_z: 
                if dialog_box_visible and game_state == "dialog":
                    if current_index < len(current_dialog) - 1:
                        current_index += 1
                    else:
                        dialog_box_visible = False

                elif game_state == "game_over":
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
                        current_dialog = cactus_happy
                        trivia_active = True
                        trivia_question_setup()
                        current_index = 0
                        dialog_box_visible = True

                
                

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
                            result_timer = pygame.time.get_ticks()
                            
                        else:
                            trivia_question_setup()
                    elif trivia_selected != correct_position:
                        cactus = cactus_points_loss
                        total_score -= 5
                        round_score -= 5
                        trivia_question_num += 1
                        if total_score < 0:
                            current_dialog = ["You have less than 0 points! Sorry, that means game over for you!"]
                            endings.append("Points Poor")
                            game_state = "game_over"
                            dialog_box_visible = True
                            current_index = 0
                            trivia_active = False
                            

                        elif trivia_question_num >= 3:
                            trivia_done = True
                            trivia_active = False
                            lines = ["That was soooo much fun!", "Till next time!", "Fun, right?", "Bye!"]
                            narrator_lines = ["That was weird.", "You are planning to play again next time, aren't you?", "Well, that is your life now."]
                            cactus_last_line = random.choice(lines)
                            narrator_last_line = random.choice(narrator_lines)
                            score_line = f"You got {round_score} points. Your total score is {total_score}!"
                            showing_trivia_result = True
                            result_timer = pygame.time.get_ticks()
                        else:
                            trivia_question_setup()     
                        

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
            dialog_character = dialog_ch
            if not dialog_box_visible and not bucket_scene_started:
                bucket_timer = pygame.time.get_ticks()
                bucket_scene_started = True
    
    if current_dialog == trivia_dialog:
        if current_index == 2:
            cactus_visible = False
            dialog_character = dialog_ch
        if current_index == len(trivia_dialog) - 1 and not dialog_box_visible and not bucket_scene_started:
            bucket_timer = pygame.time.get_ticks()
            bucket_scene_started = True

    if current_dialog == bucket_dialog:
        if current_index == 1:
            current_bg = bg2
            screen.blit(bucket_img, (510,352))

    

    if bucket_scene_started and not dialog_box_visible:
        if current_time - bucket_timer > 2000:
            current_dialog = bucket_dialog
            current_index = 0
            dialog_box_visible = True

            

    
    if game_state == "dialog":
        dialog_check()
    elif game_state == "choice_cactus_1":
        cactus_questions("That was weird", "That was soooo much fun!") 
    elif game_state == "game_over":
        dialog_check()   

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

        
            



    pygame.display.update()