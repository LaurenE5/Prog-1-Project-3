from pakudex import Pakudex

pakudex = Pakudex(capacity=5)


# Main Menu
def main():
    print()
    print('Pakudex Main Menu')
    print('-' * 17)
    print('1. List Pakuri')
    print('2. Show Pakuri')
    print('3. Add Pakuri')
    print('4. Evolve Pakuri')
    print('5. Sort Pakuri')
    print('6. Exit')
    print()
    user_input = input('What would you like to do? ')
    return user_input


if __name__ == '__main__':

    # Introduction Message
    print('Welcome to Pakudex: Tracker Extraordinaire!')

    while True:
        total_num_paku = input('Enter max capacity of the Pakudex: ')

        # Makes sure that a valid size is input
        try:
            total_num_paku = int(total_num_paku)
            if total_num_paku < 0:
                raise ValueError
            print(f'The Pakudex can hold {total_num_paku} species of Pakuri.')
            break
        except ValueError:
            print('Please enter a valid size.')
            continue

    while True:
        # Runs the main program
        user_input = main()

        # Shows a list of pakuri
        if user_input == '1':
            if pakudex.size == 0:
                print('No Pakuri in Pakudex yet!')
            else:
                print('Pakuri In Pakudex:')
                for number, element in enumerate(pakudex.get_species_array()):
                    print(f'{number + 1}. {element}')

        # shows pakuri stats
        elif user_input == '2':
            species = input('Enter the name of the species to display: ')
            for element in pakudex.pakuris:
                if element.species == species:
                    stats = pakudex.get_stats(species)
                    print('Species:', species)
                    print('Attack:', element.attack)
                    print('Defense:', element.defense)
                    print('Speed:', element.speed)
            print('Error: No such Pakuri!')

        # adds pakuri
        elif user_input == '3':
            if len(pakudex.pakuris) == total_num_paku:
                print('Error: Pakudex is full!')
                continue
            species = input('Enter the name of the species to add: ')
            if pakudex.add_pakuri(species):
                print(f'Pakuri species {species} successfully added!')

        # changes pakuri stats
        elif user_input == '4':
            species = input('Enter the name of the species to evolve: ')
            for element in pakudex.pakuris:
                if element.species == species:
                    pakudex.evolve_species(element)
                    print(f'{species} has evolved!')
                else:
                    print('Error: No such Pakuri!')

        # alphabetizes pakuri list
        elif user_input == '5':
            pakudex.sort_pakuri()
            print('Pakuri have been sorted!')

        # exits program
        elif user_input == '6':
            print('Thanks for using Pakudex! Bye!')
            exit()

        # makes sure menu selection is recognized
        else:
            print('Unrecognized menu selection!')
