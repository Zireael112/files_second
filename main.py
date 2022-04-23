def get_shop_list_by_dishes(dishes, person_count):
    cook_list = {}
    list_all = []
    for dish in dishes:
        with open('recipes.txt', encoding='utf-8') as file:
            for i in file.read().split('\n\n'):
                name, _, *args = i.split('\n')
                if dish == name:
                    list_all.append(args)

    for ls in list_all:
        for j in ls:
            a, b, c = j.split(' | ')
            cook_list[a] = {'measure': c, 'quantity': (int(b) * person_count)}
    print(cook_list)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)