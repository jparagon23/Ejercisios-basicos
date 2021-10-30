import random
 
pvictory=0
svictory=0
options=['rock','paper','scissors']

while True:
    pchoisse=input("Enter your choice or press 'Q' to stop the game: ").lower()
    schoisse=options[random.randint(0,2)]
    print('the computer chose: ',schoisse)
    print('you chose: ',pchoisse)
    if pchoisse=='q':
        print('thak you for participating')
        break
    if pchoisse not in options:
        print('you chose an invalid option')
        continue
    if schoisse==pchoisse:
        print('Tie')
    
    elif schoisse=='rock' and pchoisse=='paper':
        print(' the user wins')
        pvictory+=1

    elif schoisse=='scissors' and pchoisse=='rock':
        print(' the user wins')
        pvictory+=1


    elif schoisse=='paper' and pchoisse=='scissors':
        print(' the user wins')
        pvictory+=1
    else:
        print('you lost')
        svictory+=1
    
    
print('the system won: ',svictory,'times')
print('the user won: ',pvictory,'times')
