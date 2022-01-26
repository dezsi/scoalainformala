# daca conditie:
#   print('adevarat')
#daca alta conditie:
#   print ('nici aceasta nu e adevarata')
#altfel
#   print("afisez doar daca "conditie" si "alta conditie" nu sunt adevarate

#my_var = 5
#if my_var < 6:
#    print('set instructiuni #1')
#elif my_var < 10:
#    print("set instructiuni #2")
#else:
#    print("set instructiuni #3")
#print('a iesit')

# my_var = 7
# mesaj = "Set instructiuni #3"
# if my_var < 6:
#    mesaj = "Set innstructiuni #1"
# elif my_var < 10:
#     mesaj = "Set instructiuni #2"
#print(mesaj)
#print('a iesit')

#var = 1
#while var < 10:
#    # var = var + 1
#    print("bloc de instructiuni", var)
#    var += 1
#    #break

string = "Ana are mere"
lista = [1, 2, 3, 'a']
# for i, v in enumerate(lista):
#     print(i, '=>', v)
# for variabila_temporara in range(0, len(lista) + 1):
#     print(lista[variabila_temporara])
# print(variabila_temporara, '>>')
#dictionar = {1: 'unu', 2: 'doi', 3: 'trei'}
# for item, value in dictionar.items():
#     print(item, value)
dictionar = {'1': 'unu', '2': 'doi', '3': 'trei'}
for item in dictionar:
    print(item, dictionar.get(item))