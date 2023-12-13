from enum import Enum
import json
import os
from icecream import ic
from helper import save_list , load_list

class Actions(Enum):
    PRINT = 1
    ADD = 2
    SEARCH = 3
    DELETE = 4
    EXIT = 5

animals = []
data_file = 'animals.json'

# menu display
def menu():
    print('Welcome to my zoo!')
    for x in Actions: print(f'{x.value} - {x.name}')
    return Actions(int(input('Enter your selection :')))

# actions
def main():
    global animals
    os.system('cls' if os.name == 'nt' else 'clear')
    animals = load_list(data_file , animals)
    while(True):
        userSelection = menu()
        if userSelection == Actions.PRINT: print_animals()
        if userSelection == Actions.ADD: add_func()
        if userSelection == Actions.SEARCH: print(search_func())      
        if userSelection == Actions.DELETE: del_func()
        if userSelection == Actions.EXIT: exit_func()


# print animals
def print_animals():
    for animal in animals:
        ic(animal)


# add animal
def add_func():
    animals.append({'name' : input('animal name: ') , 'age' : input('animal age: ') , 'type' : input('animal type: ')})
    print('animal added!')

# exit
def exit_func():
    print('Bye')
    save_list(data_file , animals)
    exit()

# search for animal
def search_func():
    global animals
    find_animal = input('Enter animal name: ')
    for animal in animals:
        if animal['name'] == find_animal:
            return animal
    print('animal was not found...')

# delete animal
def del_func():
    global animals
    del_animal = input('Enter animal to remove: ')
    for animal in animals:
        if animal['name'] == del_animal:
            animals.remove(animal)
            print(f'{del_animal} has been removed.')
            return

if __name__ == '__main__':
    main()