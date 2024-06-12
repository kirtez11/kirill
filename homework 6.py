my_dict = { 'Kir': 1996, 'Alex': 1995, 'Sasha': 1997 }
print(my_dict['Kir'] )
print(my_dict.get('Kira') )
my_dict.update({'Misha': 1990,
                'Masha': 1993})
print(my_dict.pop('Misha'))
print(my_dict)



my_set = {'a', 1, 1, 'a', 3.14}
print(my_set)
my_set.update([2, 'b'])
my_set.discard(2)
print(my_set)
