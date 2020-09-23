

def welcome():

    print('Welcome to my first python test')

    name = input('what is your name? >>> ')

    print('Hello,',name, 'Nice to meet you.')

    whereFrom = input('Where are you from? >>> ')

    print('Wow that is a cool place, I just visited', whereFrom + ',', 'met some nice computers there.')
    nextStep()


def nextStep():
    print('this is the next step...')
    answer = input('Are you ready?? type (yes or no) >>>')
    if answer == 'Yes' or answer == 'yes':
        print('Ok. lets get started')
        stepThree()
    else: 
        print('Well, maybe next time then')
        goodBye()

def stepThree():
    answer = input('what is 2 + 3 ??? >>> ')
    if answer == '5':
        print('good job.')
        goodBye()
    else:
        print('you dumb bitch.')
        goodBye()

def goodBye():
    print('see you next time!')

welcome()