def send_email(message, recipient, sender = "university.help@gmail.com"):
        
# Проверка на корректность e-mail отправителя и получателя
    if '@' not in recipient or not recipient.endswith(('.com', '.ru', '.net')) or '@' not in sender or not sender.endswith(('.com', '.ru', '.net')):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
        
# Проверка на отправку самому себе
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")

# Проверка на отправителя по умолчанию
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.") 
    
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
        
# Вывод результатов
send_email('message', 'vasyok1337@gmail.com')
send_email('message', 'urban.fan@mail.ru', 'urban.info@gmail.com')
send_email('message', 'urban.student@mail.ru', 'urban.teacher@mail.uk')
send_email('message', 'university.help@gmail.com', 'university.help@gmail.com')
