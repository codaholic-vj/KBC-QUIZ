print('Welcome to KBC!(Kaun Banega Crorepati)')

playing = input('Do you want to play? ')

if playing.upper() != 'YES':
    quit()

print("Okay! let's play :)")
score = 0
answer = input('what is the fullform of IAS? ')
if answer.lower() == 'indian administrative service':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('which city is known as silicon valley of india? ')
if answer.lower() == 'bangalore':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('which river is located in Ayodhya city? ')
if answer.lower() == 'saryu river':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('Kedarnath is located in which state? ')
if answer.lower() == 'uttrakhand':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('what is the length of ganga river? ')
if answer.lower() == '2525 km':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('where is jewar airport located? ')
if answer.lower() == 'uttar pradesh':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('who is known as nightingale of india? ')
if answer.lower() == 'lata mangeshkar':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('which day is celebrated as yoga day? ')
if answer.lower() == '21 june':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('in  which year india won its first cricket world cup? ')
if answer.lower() == '1983':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('which  country held G20 summit in 2023? ')
if answer.lower() == 'india':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print('You got ' + str(score) + ' questions correct!')
print('You got ' + str((score / 4) *100) + ' %.')

