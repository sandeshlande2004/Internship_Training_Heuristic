import random

title = 'Welcome to Kon Banega Crorepati'
print(title.center(50, '-'))
sub_title = 'Win a crore by answering simple questions'
print(sub_title.center(50))
print('\n')

questions = {
    'What is the capital of France?': {
        "options": ['Paris', 'London', 'Berlin', 'New York'],
        "answer": 'Paris'
        },
    'Who is the founder of Microsoft?': {
        "options": ['Bill Gates', 'Steve Jobs', 'Mark Zuckerberg', 'Elon Musk'],
        "answer": 'Bill Gates'
        },
    'Which is the largest planet in our solar system?': {
        "options": ['Earth', 'Jupiter', 'Saturn', 'Mars'],
        "answer": 'Jupiter'
        },
    'What is the currency of Japan?': {
        "options": ['Yen', 'Dollar', 'Euro', 'Pound'],
        "answer": 'Yen'
        },
    'Which is the most wining team in IPL?': {
        "options": ['MI', 'CSK', 'KKR', 'RCB'],
        "answer": 'MI'
        },
    'What is the full form of CPU?': {
        "options": ['Central Processing Unit', 'Central Process Unit', 'Computer Personal Unit', 'Central Processor Unit'],
        "answer": 'Central Processing Unit'
        },
    'Which is the longest river in the world?': {
        "options": ['Nile', 'Amazon', 'Ganga', 'Yangtze'],
        "answer": 'Nile'
        }
}

while True:
    name = input('Enter your name: ')
    mob = input('Enter your mobile number: ')
    print('\n')
    question = random.choice(list(questions.keys()))
    print(question)
    print('Options:')
    for i, option in enumerate(questions[question]['options'], 1):
        print(f"{i}. {option}")
    print('\n')
    user_answer = int(input('Enter your choice: '))
    user_answer = questions[question]['options'][user_answer - 1].lower()   
    
    if user_answer == questions[question]['answer'].lower():
        print('Correct Answer! You win!')
        print(f"Congratulations {name}! You have won 1 crore.")
    else:
        print('Wrong Answer! You lose!')
        correct_answer = questions[question]['answer']
        print(f"Correct answer is: {correct_answer}")
    print('\n')
    play_again = input('Do you want to play again? (yes/no): ')
    if play_again.lower() != 'yes':
        break
