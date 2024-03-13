def main ():
    while True:
        userNumber  = get_integer('Enter a number:\n')
        if (userNumber %  2 == 0):
            print('The number is even!')
        else:
            print('The number is odd!')
        print('Do you want to do it again?')
        again = input('enter \'y\' to loop again: ')
        if again != 'y':
            break
    print('The loop has ended.')
    
def get_integer(message):
    while True:
        try:
            user_input = int(input(message))
            return user_input
        except ValueError:
            print('Incorrect data entered, please re-attempt')
main()
                      
