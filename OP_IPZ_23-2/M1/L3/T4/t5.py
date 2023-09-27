'''
Напишіть програму, яка зчитує ціле число і виводить текст, 
аналогічний наведеному в прикладі (прогалини і точки важливі!).

#TODO
output:
Після числа 5 йде число 6.
Перед числом 5 йде число 4.

'''

number=int(input("integer number:"))
numberNext=number+1
numberPreve=number-1

print(f"Після числа {number} йде число {numberNext}.")
print(f"Перед числом {number} йде число {numberPreve}.")