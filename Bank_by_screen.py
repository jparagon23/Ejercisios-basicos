exit='y'
pass_att=3
password=9809
print('Welcome to JPS atm')
balance=958000


while pass_att>0:
    int_password=int(input('Please introduce your password: '))
    if int_password==password:
        print('your password is correct')
        while exit not in ('n','no'):
            print('Please press 1 to see your balance')
            print('Please press 2 to make a withdraw')
            print('Please press 3 to deposit money')
            print('Please press 4 to return the card')
            option1=int(input('what would you like to choose?: '))
            if option1==1:
                print( 'your balance is: $',balance)
                exit=input('will  you like to go back?: ')
            elif option1==2:
                while True:
                    print('How much money would you like to withdraw')
                    print('1:$50.000')
                    print('2:$100.000')
                    print('3:$200.000')
                    print('4:Another value')
                    posible_withdraw={1:50000,2:100000,3:200000,4:'other'}
                    withdraw=int(input('Please make a choice: '))
                    if withdraw in [1,2,3]:
                        balance=balance-posible_withdraw[withdraw]
                        print('Please take the money')
                        print('Your new balance is $',balance)
                        exit=input('will  you like to go back?: ')
                        break
                    if withdraw ==4:
                        withdraw_manual= int(input('how much money would you like to withdraw? '))
                        balance=balance-withdraw_manual
                        print('Your new balance is $',balance)
                        exit=input('will  you like to go back?: ')
                        break
                    else:
                        print('You selected and invalid number, please try again')
                        continue

            elif option1==3:
                deposit=int(input('How much money would you like to deposit?: '))
                balance=balance+deposit
                print('your new balance is $',balance)
                exit=input('will  you like to go back?: ')
            elif option1==4:
                print('wait a second...')
                print('you can remove the card')
                break
        print('Thank you for trusting us, good bye')
        break
    else:
        pass_att-=1
        print('Your password is not correct, you have',pass_att,'attemps left')
if pass_att==0:
     print('Your card has been blocked')