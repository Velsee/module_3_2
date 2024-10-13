# Вынесение синтаксической проверки в отдельную функцию
def is_valid_email(email):
    email = email.lower()
    return "@" not in email or not email.endswith((".com", ".ru", ".net"))

def send_email(message, recipient, sender="university.help@gmail.com"):
    recipient = recipient.lower()
    sender = sender.lower()

    # Проверка на корректность e-mail отправителя и получателя
    if is_valid_email(recipient) or is_valid_email(sender):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

    # Проверка на отправку самому себе
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")

        # Проверка на отправителя по умолчанию
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")

    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email('message', 'vasyok1337@gmail.com')
send_email('message', 'urban.fan@mail.ru', 'urban.info@gmail.com')
send_email('message', 'urban.student@mail.ru', 'urban.teacher@mail.uk')
send_email('message', 'university.help@gmail.com', 'university.help@gmail.com')
