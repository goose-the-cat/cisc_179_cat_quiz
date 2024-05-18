import random
import time

# Initialize total score, incorrect attempts counter, and hints used counter
total_score = 0
incorrect_attempts = [0] * 8  # Track incorrect attempts for each question
hints_used = 0  # Track the number of hints used

# List of correct answers
correct_answers = ('Nala', 'Maine Coon', '1963', 'Stubbs', 'Isaac Newton', 'Nose', 'Clowder', 'Sweet')

# Corresponding questions
questions = ('Who is the richest cat in the world?', 
             'What is the largest domestic cat breed?', 
             'The first cat went to space October 18,', 
             'This cat was mayor for an Alaskan town for 20 years.', 
             'This famous scientist invented the cat door.', 
             'Like a fingerprint, cats have a ____ print.', 
             'A group of cats is called a?', 
             'Cats lack this taste bud.')

# Multiple-choice options for each question
multiple_choices = [
    ['Grumpy Cat', 'Nala', 'Tom', 'Garfield'],
    ['Persian', 'Siamese', 'Maine Coon', 'Bengal'],
    ['1957', '1961', '1963', '1965'],
    ['Tom', 'Stubbs', 'Felix', 'Simba'],
    ['Albert Einstein', 'Isaac Newton', 'Galileo', 'Nikola Tesla'],
    ['Nose', 'Ear', 'Paw', 'Tail'],
    ['Pack', 'Pride', 'Clowder', 'Herd'],
    ['Salty', 'Bitter', 'Sweet', 'Sour']
]

# Hints for each question
hints = ('She is an Instagram star.', 
         'It is known for its size and fur.', 
         'Think of a year in the 1960s.', 
         'A fictional name of a dog, but for a cat.', 
         'An apple fell on his head.', 
         'It is on their face.', 
         'It sounds like cloud.', 
         'Think of something sugary.')

# Number of questions
number_questions = len(correct_answers)

# Create a list of indices representing each question, then shuffle to randomize order
question_indices = list(range(number_questions))
random.shuffle(question_indices)

# Prompt user to choose between multiple-choice and written answer
mode = input("Would you like to answer in 'multiple-choice' or 'written' mode?\n").strip().lower()

# If written mode is selected, prompt the user to choose if they want a timer
if mode == 'written':
    timer_enabled = input("Would you like to enable a 15-second timer for each question? (yes/no)\n").strip().lower()
else:
    timer_enabled = 'no'  # Default to 'no' if not in written mode

# Prompt user to choose the number of tries per question
tries = input("How many tries would you like for each question?\n").strip()
tries = int(tries) if tries.isdigit() and int(tries) > 0 else 1  # Ensure at least 1 try

def ask_question(question_number):
    """
    Function to ask a single question.
    Parameters:
        question_number (int): The index of the question to be asked.
    Returns:
        bool: True if the answer was correct, False otherwise.
    """
    global total_score, hints_used  # Use the global variables
    idx = question_indices[question_number]  # Get the index of the current question
    print(f"\nQuestion {question_number + 1}: {questions[idx]}")
    
    attempts = 0  # Initialize attempt counter
    
    if mode == 'multiple-choice':
        # Display multiple-choice options
        options = multiple_choices[idx]
        random.shuffle(options)  # Shuffle the multiple-choice options
        
        for i, option in enumerate(options):
            print(f"{i + 1}. {option}")
        
        while attempts < tries:
            # Prompt user to enter their answer
            answer = input("\nEnter the number of your answer (or type 'hint' for a hint):\n")
            
            if answer.lower() == 'hint':
                print(f"Hint: {hints[idx]}")
                hints_used += 1
                continue  # Re-ask the same question with the hint
            
            if answer.isdigit() and int(answer) in range(1, 5):
                selected_option = options[int(answer) - 1]
                if selected_option.lower() == correct_answers[idx].lower():
                    print('Correct!')
                    total_score += 1  # Increment the score if correct
                    return True
                else:
                    attempts += 1  # Increment the attempt counter
                    incorrect_attempts[idx] += 1  # Increment the incorrect attempts counter for that question
                    print('Incorrect!')
                    if attempts < tries:
                        print(f"Try again. You have {tries - attempts} tries left.")
                    else:
                        print(f'The correct answer is {correct_answers[idx]}')
                        return False
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
    else:
        # Written answer mode
        start_time = time.time()  # Record the start time for timing the response
        
        while attempts < tries:
            # Prompt user to enter their answer
            answer = input("\nEnter your answer (or type 'hint' for a hint):\n").strip()
            
            if answer.lower() == 'hint':
                print(f"Hint: {hints[idx]}")
                hints_used += 1
                continue  # Re-ask the same question with the hint
            
            # Check if timer is enabled and if the elapsed time exceeds 15 seconds
            if timer_enabled == 'yes':
                elapsed_time = time.time() - start_time  # Calculate elapsed time
                if elapsed_time > 15:
                    print('Time is up!')  # Notify the user if they took too long
                    return False
            
            if answer.lower() == correct_answers[idx].lower():
                print('Correct!')
                total_score += 1  # Increment the score if correct
                return True
            else:
                attempts += 1  # Increment the attempt counter
                incorrect_attempts[idx] += 1  # Increment the incorrect attempts counter for that question
                print('Incorrect!')
                if attempts < tries:
                    print(f"Try again. You have {tries - attempts} tries left.")
                else:
                    print(f'The correct answer is {correct_answers[idx]}')
                    return False

# Ask each question in the randomized order
for i in range(number_questions):
    ask_question(i)

# Print the final score and the number of hints used
print(f'\nYour total score is: {total_score}/{number_questions}')
print(f'You used {hints_used} hints.')

# Print the number of incorrect attempts for each question
print('\nIncorrect attempts per question:')
for i, attempts in enumerate(incorrect_attempts):
    print(f'Question {i + 1}: {attempts} incorrect attempts')

# Provide feedback based on the total score
if total_score == number_questions:
    print("\nExcellent! You got all the questions right!")
elif total_score >= number_questions / 2:
    print("\nGood job! You know your cat trivia well.")
else:
    print("\nYou might want to learn more about cats.")
