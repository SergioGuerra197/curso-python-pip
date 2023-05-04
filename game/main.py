import random


def choose_options():

    options = ('piedra', 'papel', 'tijeras')

    user_option = input('Piedra, papel o tijeras => ').lower()

    if not user_option in options:

        print('La opción seleccionada no esta en las opciones correctas')

        return 'INCORRECT', 'OPTION'

    computer_option = random.choice(options)

    print('Opcion usuario => ', user_option)

    print('Opcion computador => ', computer_option)

    return user_option, computer_option


def rules(user_option, computer_option, user_wins, computer_wins):

    if user_option == computer_option:

        print('Empate!, ambos tienen la misma opción')

    elif user_option == 'piedra':

        if computer_option == 'tijeras':

            print('Usuario ganó!!, Piedra gana a tijeras')

            user_wins += 1

        else:

            print('Computadora ganó!!, Papel gana a piedra')

            computer_wins += 1

    elif user_option == 'papel':

        if computer_option == 'piedra':

            print('Usuario ganó!!, Papel gana a piedra')

            user_wins += 1

        else:

            print('Computadora ganó!!, tijeras gana a papel')

            computer_wins += 1

    elif user_option == 'tijeras':

        if computer_option == 'papel':

            print('Usuario ganó!!, Tijeras gana a papel')

            user_wins += 1

        else:

            print('Computadora ganó!!, Piedra le gana a tijeras')

            computer_wins += 1

    return user_wins, computer_wins


def run_game():

    user_wins = 0

    computer_wins = 0

    rounds = 0

    while True:

        rounds += 1
        print('*' * 30)
        print('ROUND =>', rounds)
        print('*' * 30)

        print('Computer_wins =>', computer_wins)
        print('user_wins =>', user_wins)

        user_option, computer_option = choose_options()

        user_wins, computer_wins = rules(
            user_option, computer_option, user_wins, computer_wins)

        if computer_wins == 2:

            print('Computer_wins =>', computer_wins)

            print('Computadora ganó')

            break

        if user_wins == 2:

            print('user_wins =>', user_wins)

            print('Usuario ganó')

            break


run_game()
