'''
Кількість секунд
кількість секунд у році.
Напишіть програму, яка рахує і друкує, скільки секунд в році, в якому 365 діб

Зверніть увагу:
1 рік = 365 днів
1 день = 24 години
1 година = 60 хвилин
1 хвилина = 60 секунд

(Перемножує кількість секунд в хвилині, хвилин в годині, годин у добі, діб у році).
'''

yers=int(input("кількість років:"))

if(yers>0):
    #кількість секунд в одному році
    sec=365*24*60*60
    manyYersOrNot="роках" if yers>1 else "році"
    secondsYers=sec*yers
    print(f"в {yers} {manyYersOrNot} {secondsYers}секунд")