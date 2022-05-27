import random

choice = [ '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''', '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''', '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']
while input('Want to continue Type "false to stop" or anything else to continue: ') != 'false':
    human_choice = int(input('What is your choose? Type "0"  for Rock, "1"  for Paper, "2" for Scissors.'))
    computer_choice = random.randint(0, 2)


    def who_win(computer, human):

        if human == computer:
            print('draw')
        elif choice[human-1] == choice[computer]:
            print('You win!')
        else:
            print('You lose')


    print(choice[human_choice])
    print(f"Computer chose: \n {choice[computer_choice]}")
    who_win(computer_choice, human_choice)

