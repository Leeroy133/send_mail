import smtplib
import os

from dotenv import load

load()

website = 'https://dvmn.org/referrals/i7iQz20ghmw3Lig1dUOk0B1kzJwSktCx6f2Swt8Z/'
sender_name = 'Никита'
recipient_name = "Михаил"
sender_email = 'laraxsmurf@yandex.ru'
recipient_email = 'nikita.kozytenko@yandex.ru'
subject = 'Приглашение!'
content_type = 'text/plain; charset=''"''UTF-8''"'

letter = """\
From: {sender_email}
To: {recipient_email}
Subject: {subject}
Content-Type: {content_type};


Привет, {recipient_name}! {sender_name} приглашает тебя на сайт {website}!

{website} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {website}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {website}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""" .format(website=website, sender_name=sender_name, recipient_name=recipient_name, sender_email=sender_email, recipient_email=recipient_email, subject=subject, content_type=content_type)

letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(os.getenv('LOGIN'), os.getenv('PASSWORD'))
server.sendmail(sender_email, recipient_email, letter)
server.quit()
