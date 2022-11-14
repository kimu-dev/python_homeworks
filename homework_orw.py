from pprint import pprint

recipes = 'recipes.txt'

def book_recipes(recipes):
    with open(recipes, encoding = 'utf-8') as file_obj:
        cook_book = {}
        for line in file_obj:
            dish = line.strip()
            ingredients = []
            for obj in range(int(file_obj.readline())):
                ingredient = file_obj.readline()
                ing_list = []
                ing_dict = {}
                for obj_1 in ingredient.split(sep = '|'):  
                    ing_list.append(obj_1.strip())
                ing_dict['ingredient_name'] = ing_list[0]
                ing_dict['quantity'] = ing_list[1]
                ing_dict['measure'] = ing_list[2]
                ingredients.append(ing_dict)
            cook_book[dish] = ingredients
            file_obj.readline()
        return cook_book

pprint(book_recipes(recipes))

def get_shop_list_by_dishes(dishes, person_count):
    recipe = book_recipes(recipes)
    c = {}
    for dish in recipe.keys():
        if dish in dishes:
            for ing in recipe[dish]:
                ik = list(ing.keys())
                iv = list(ing.values())
                k = (ik[2], ik[1])
                v = (iv[2], int(iv[1]) * person_count)
                kv = list(zip(k, v))
                c[iv[0]] = dict(kv)
    return c

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 3))

# def get_shop_list_by_dishes(dishes, person_count):
#     recipes = book_recipes(recipes)
#     for dish in recipes:
#         print(dish)

# ing = 'Яйцо | 2 | шт'

# ing_list = []
# ing_dict = {}
# for i in ing.split(sep = '|'):
#     ing_list.append(i)
# ing_dict['ingredient_name'] = ing_list[0]
# ing_dict['quantity'] = ing_list[1]
# ing_dict['measure'] = ing_list[2]
# print(ing_list)
# print(ing_dict)

# print(sorted(list_sort, key = ))
 
# for txt in files:
#     with open(txt, 'r', encoding = 'utf-8') as file_obj_r:
#         line = file_obj_r.readlines()
#         print(len(line))

# files = [
#     r'C:\Users\predator\Desktop\homeworks\sorted\1.txt', 
#     r'C:\Users\predator\Desktop\homeworks\sorted\2.txt', 
#     r'C:\Users\predator\Desktop\homeworks\sorted\3.txt'
#         ]

# file_w = r'C:\Users\predator\Desktop\homeworks\sorted\all.txt'

# with open(file_w, 'a', encoding = 'utf-8') as file_obj_a:
#     for txt in files:
#         with open(txt, encoding = 'utf-8') as file_obj_r:
#             a = '\\'
#             b = {}
#             file_obj_a.write(f'{txt.split(a)[-1]}\n') 
#             line_r = file_obj_r.readlines()
#             line_l = len(line_r)
#             file_obj_a.write(f'{str(line_l)}\n') 
#             with open(txt, encoding = 'utf-8') as file_obj_r:
#                 for line in file_obj_r:
                    
#                     file_obj_a.write(f'{line.strip()}\n') 
#                 file_obj_a.write('\n')

# with open(file_w, 'a', encoding = 'utf-8') as file_obj_a:
#     for txt in files:
#         with open(txt, 'r', encoding = 'utf-8') as file_obj_r:
#             a = '\\'
#             c = []
#             b = {}
#             b['name_file'] = f'{txt.split(a)[-1]}'
#             for line in file_obj_r:
#                 c.append(f'{line.strip()}')
#                 b['line_count'] = len(c)
#                 b['text'] = ' '.join(c)
#         print(b)

def write_all():
    files = [
    r'C:\Users\predator\Desktop\homeworks\sorted\1.txt', 
    r'C:\Users\predator\Desktop\homeworks\sorted\2.txt', 
    r'C:\Users\predator\Desktop\homeworks\sorted\3.txt'
            ]
    file_w = r'C:\Users\predator\Desktop\homeworks\sorted\all.txt'

    with open(file_w, 'a', encoding = 'utf-8') as file_obj_a:
        d = {}
        for txt in files:
            with open(txt, 'r', encoding = 'utf-8') as file_obj_r:
                a = '\\'
                d[f'{txt.split(a)[-1]}'] = str(len(file_obj_r.readlines()))
        d_sorted = dict(sorted(d.items(), key = lambda item: item[1]))
        # print(d_sorted)

        dd = {}
        for txt in files:
            with open(txt, 'r', encoding = 'utf-8') as file_obj_r:
                a = '\\'
                dd[f'{txt.split(a)[-1]}'] = file_obj_r.read()
        # print(dd)

        for dict_k, dict_v in d_sorted.items():
            file_obj_a.write(f'{dict_k}\n') 
            file_obj_a.write(f'{dict_v}\n') 
            if dict_k in dd:
                file_obj_a.write(f'{dd[dict_k]}\n') 
            file_obj_a.write('\n')

write_all()

