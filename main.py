total_score = 0
correct_answers = ('Nala', 'Maine Coon', '1963', 'Stubbs', 'Isaac Newton', 'Nose', 'Clowder', 'Sweet')
questions = ('Who is the richest cat in the world', 'What is the largest domestic cat breed', 'The first cat went to space October 18, ', 'This cat was mayor for an Alaskan town for 20 years', 'This famous scientist invented the cat door', 'Like a fingerprint, cats have a ____ print', 'A group of cats is called a', 'Cats lack this taste bud')
number_questions = len(correct_answers)

for question_number in range(1, number_questions + 1):
  print(f"Question {question_number}: {questions[question_number-1]}")
  answer = input("Enter your answer:")
  
  if answer.lower() == correct_answers[question_number-1].lower():
    print('Correct!')
    total_score += 1
  else:
    print('Incorrect!')
    print(f'The correct answer is {correct_answers[question_number-1]}')

print(f'Your total score is: {total_score}/{number_questions}')
