import random


items_not_weapon = []
weapons = ['lasrifle', 'shotgun', 'boltgun', 'knife']


def starting_position():
    start_place = ['Cell block', 'Engine', 'Medical bay']
    game_start_place = random.choice(start_place)

    if game_start_place == 'Cell block':
        hero_class = 'prisoner'
    elif game_start_place == 'Engine':
        hero_class = 'Adeptus Mechanicus'
    elif game_start_place == 'Medical bay':
        hero_class = 'Guardsman'

    return hero_class





def search(item_list):
    inventory = {
        'weapon': 0,
        'tool': 0,
        'armor': 0,

    }


def starter():

    pass




def main_way():
    pass




def main():
    starting_position()
    print(starting_position())

if __name__ == '__main__':
    main()

