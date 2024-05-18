import random
import time

# Initialize total score, incorrect attempts counter, and hints used counter
total_score = 0
incorrect_attempts = [0] * 8
hints_used = 0

# List of correct answers
correct_answers = ('Nala', 'Maine Coon', '1963', 'Stubbs', 'Isaac Newton', 'Nose', 'Clowder', 'Sweet')

# Corresponding questions
questions = ('Who is the richest cat in the world', 
             'What is the largest domestic cat breed', 
             'The first cat went to space October 18, ', 
             'This cat was mayor for an Alaskan town for 20 years', 
             'This famous scientist invented the cat door', 
             'Like a fingerprint, cats have a ____ print', 
             'A group of cats is called a', 
             'Cats lack this taste bud')

# Hints for each question
hints = ('She is an Instagram star', 
         'It is known for its size and fur', 
         'Think of a year in the 1960s', 
         'A fictional name of a dog, but for a cat', 
         'An apple fell on his head', 
         'It is on their face', 
         'It sounds like cloud', 
         'Think of something sugary')

# Number of questions
number_questions = len(correct_answers)

# Create a list of indices representing each question, then shuffle to randomize order
question_indices = list(range(number_questions))
random.shuffle(question_indices)

def ask_question(question_number):
    """
    Function to ask a single question.
    Parameters:
        question_number (int): The index of the question to be asked.
    Returns:
        bool: True if the answer was correct, False otherwise.
    """
    global total_score, hints_used  # Use the global variables
    print(f"Question {question_number + 1}: {questions[question_indices[question_number]]}")
    
    start_time = time.time()  # Record the start time for timing the response
    while True:
        answer = input("Enter your answer (or type 'hint' for a hint): ")
        
        # Provide hint if the user types 'hint'
        if answer.lower() == 'hint':
            print(f"Hint: {hints[question_indices[question_number]]}")
            hints_used += 1  # Increment the hints used counter
            continue
        
        elapsed_time = time.time() - start_time  # Calculate elapsed time
        if elapsed_time > 15:
            print('Time is up!')  # Notify the user if they took too long
            return False
        
        # Check if the user's answer is correct
        if answer.lower() == correct_answers[question_indices[question_number]].lower():
            print('Correct!')
            total_score += 1  # Increment the score if correct
            return True
        else:
            # If the answer is incorrect, increment the incorrect attempts counter for that question
            incorrect_attempts[question_indices[question_number]] += 1
            print('Incorrect!')
            print(f'The correct answer is {correct_answers[question_indices[question_number]]}')
            return False

# Ask each question in the randomized order
for i in range(number_questions):
    ask_question(i)

# Print the final score and the number of hints used
print(f'Your total score is: {total_score}/{number_questions}')
print(f'You used {hints_used} hints.')

# Print the number of incorrect attempts for each question
print('Incorrect attempts per question:')
for i, attempts in enumerate(incorrect_attempts):
    print(f'Question {i + 1}: {attempts} incorrect attempts')

# Provide feedback based on the total score
if total_score == number_questions:
    print("Excellent! You got all the questions right!")
elif total_score >= number_questions / 2:
    print("Good job! You know your cat trivia well.")
else:
    print("You might want to learn more about cats.")
