'''
Вільний діалог

Вільне завдання: вигадайте свою програму, яка задає питання і коментує відповіді.
Можна, наприклад, написати програму-анкету, яка запитує дані людини: ім'я, прізвище, вік, улюблені колір 
і страву і т. д., а потім друкує табличку типу 
"Ім'я: (ім'я людини)". 
"Прізвище: (введене прізвище)" 
і т. д.            
                                                                                  
А можна придумати смішний діалог. 
Запропонуйте друзям поговорити з цією програмою!
'''

userData={
    "ПІБ":input("ПІБ:"),
    "Пароль":input("Пароль:"),
    "Вік":input("Вік:"),
    "електронна пошта":input("електронна пошта:")
}

for key in userData:
    print(f"{key}:"+userData[key])
