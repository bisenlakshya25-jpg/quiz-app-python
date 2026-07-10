#================/@/==================
#.         import the modules 
#.         defining universal things
#================/@/==================

import os
import json
import random

FILE_NAME = "questions.json"
questions = {}

#================/@/==================
# file handling
#================/@/==================

#To load data
def load_data():
    global questions 
    
    if os.path.exists(FILE_NAME):
        
        try:
            with open(FILE_NAME, "r") as file:
                data = json.load(file)
                questions = {k: v for k, v in data.items()}
                
        except Exception as e:
            print(f"❌ Error loading Data : {e}")
    
    else:
        questions = {}
    


#================/@/==================
# INPUT VALIDATION
#================/@/==================

def check_input(prompt, max_val = 10, min_val = 1, allow_quit = False):
    print(" ")
    
    while True:
        value = input(prompt)
        value = value.strip().lower()
        
        if allow_quit and value == "q":
            return "q"
        
        try:
            num = int(value)
            
            if min_val <= num <= max_val:
                return num
            
            else:
                print("Invalid input! Please enter a value between", min_val, "and", max_val)
        
        except ValueError:
          print("Invalid input! Please enter a valid integer.")


#================/@/==================
# CONVENIENT FEATURES
#================/@/==================


def check_database():
    if not questions:
        print("No questions found in the database")
        return False
    
    return True

#-------------------------------------------

def game_end():
    print("\n1. Return to main menu\n2. Exit")
    user_choice = check_input("Enter your choice:", max_val = 2)
    
    if user_choice == 1:
      return True
    
    else:
      return False


#================/@/==================
# QUIZ SETUP
#================/@/==================

def feedback(score_percent):
    
    if score_percent >= 90:
        print("Bravo🙀keep going like this")
    
    elif score_percent >= 80:
        print("Excellent score! keep practicing")
    
    elif score_percent >= 60:
        print("Good score! Needs practice")
    
    elif score_percent >= 40:
        print("Average🙂No worries just practice ")
    
    else:
        print("You failed🥺 Don't worry keep practicing ")
    
    return  
    
#-------------------------------------------

def show_result(category, difficulty, correct_answer, wrong_answer, skipped_answer):
    
    combined = wrong_answer + skipped_answer
    total_ques = len(correct_answer) + len(combined)
    
    marking = questions[category][difficulty]["marking"]
    correct = float(marking["correct"])
    wrong = float(marking["wrong"])
    
    final_score = (len(correct_answer) * correct) - (len(wrong_answer) * wrong)
    total_score = total_ques * correct
    
    accuracy = (len(correct_answer) * 100) / total_ques
    score_percent = (final_score * 100) / total_score
    
    print(f"Your final score is {final_score} out of {total_score}")
    feedback(score_percent)
    print(f"Total questions: {total_ques}\nCorrect answers: {len(correct_answer)}\nWrong/Skipped: {len(combined)}\nAccuracy: {accuracy}%")
    
    print("________________________________________")
    if combined:
        print("let's check the answers of wrong and skipped questions")
        combined = wrong_answer + skipped_answer
    
        for que in combined:
            print(f"Q: {questions[category][difficulty]["questions"][que]['question']}")
            print(f"Correct Answer: {questions[category][difficulty]["questions"][que]['answer']}")
            print("__________________________________")
    
    user_next = check_input("1. Return to main menu\n2. Exit", max_val = 2)
    if user_next == 1:
        return True
    
    else:
        return False
            
#-------------------------------------------

def check_result(category, difficulty, answer):
    
    correct_answer = []
    wrong_answer = []
    skipped_answer = []
    
    for que, ans in answer.items():
        if questions[category][difficulty]["questions"][que]["answer"] == ans:
            correct_answer.append(que)
        
        elif ans == "q":
            skipped_answer.append(que)
        
        else:
            wrong_answer.append(que)
    
    return show_result(category, difficulty, correct_answer, wrong_answer, skipped_answer)

#-------------------------------------------

def quiz_run(category, difficulty, num_questions):
    
    list_question = list(questions[category][difficulty]["questions"].keys())
    selected_questions = random.sample(list_question, num_questions)
    
    que_no = 1
    answer = {}
    
    for que in selected_questions:
        print(f"Q.{que_no}: {questions[category][difficulty]["questions"][que]["question"]}")
        
        for num, option in questions[category][difficulty]["questions"][que]["options"].items():
            print(f"{num}. {option}")
        
        user_answer = check_input("Enter choice: ", max_val = 4, allow_quit = True)  
        answer[que] = str(user_answer)
        que_no += 1
        print("________________________________________")
    
    return check_result(category, difficulty, answer)

#-------------------------------------------

def quiz_start():
    if not check_database():
        return False
    
    print("")
    print("________________________________________")
    print("Please select the topic for the quiz")
    
    category = list(questions.keys())
    count = 1
    
    for item in category:
        print(f"{count}. {item}")
        count += 1
    
    user_choice = check_input("Enter Choice: ", max_val = len(category), allow_quit = True)
    if user_choice == "q":
        return game_end()
    
    category = category[user_choice - 1]
    print("________________________________________")
    print("Please select the difficulty level")
    
    difficulty = list(questions[category].keys())
    count = 1
    
    for item in difficulty:
        print(f"{count}. {item}")
        count += 1
    
    user_choice = check_input("Enter Choice: ", max_val = len(difficulty), allow_quit = True)
    if user_choice == "q":
        return game_end()
    
    difficulty = difficulty[user_choice - 1]
    
    print("________________________________________")
    total_questions = len(list(questions[category][difficulty]["questions"].keys()))
    print(f"Category: {category}\nDifficulty: {difficulty}\nAvailable Questions: {total_questions}")
    print("(Minimum 5 questions)")
    
    user_select = check_input("Please enter the number of question: ", max_val = total_questions, min_val = 5, allow_quit = True)
    if user_select == "q":
        return game_end()
    
    return quiz_run(category, difficulty, user_select)



#================/@/==================
# RULE BOOK
#================/@/==================


def show_rules():
    print("======================================")
    print("            QUIZ RULES")
    print("======================================")
    print("1. Select your preferred quiz category.")
    print("2. Choose a difficulty level.")
    print("3. Select the number of questions to attempt (Minimum: 5).")
    print("4. Enter the option number (1-4) to answer each question.")
    print("5. Enter 'Q' anytime to skip the current question.")
    print("6. Marks will be awarded according to the selected quiz's marking scheme.")
    print("7. Negative marking may apply, depending on the quiz.")
    print("8. At the end of the quiz, your score, accuracy, and performance will be displayed.")
    print("9. Correct answers for all wrong or skipped questions will be shown.")
    print("10. Enjoy the quiz and keep learning!")
    print("======================================")

    user_choice = check_input("1. Play the game\n2. Return to main menu\n3. Exit\nEnter choice: ", max_val=3)

    if user_choice == 1:
        return quiz_start()
    
    elif user_choice == 2:
        return True
    
    else:
        return False


#================/@/==================
# MAIN MENU
#================/@/==================

def main_menu():
    print("======================================")
    print("QUIZ GAME")
    print("======================================")
    print("")
    
    user_input = check_input("1. START QUIZ \n2. Show rules\n3. Exit", max_val = 3)
    if user_input == 1:
        return quiz_start()
    
    elif user_input == 2:
        return show_rules()
    
    else:
        return False


#================/@/==================
# GAME STARTER
#================/@/==================

load_data()
while True:
    if not main_menu():
        print("Thanks for playing see you soon❤️")
        break



