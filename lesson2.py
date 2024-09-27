import smtplib
import os

from dotenv import load

load()

website = 'https://dvmn.org/referrals/i7iQz20ghmw3Lig1dUOk0B1kzJwSktCx6f2Swt8Z/'
my_name = 'Никита'
friend_name = "Михаил"
mail_from = 'laraxsmurf@yandex.ru'
mail_to = 'nikita.kozytenko@yandex.ru'
subject = 'Приглашение!'
content_type = 'text/plain; charset=''"''UTF-8''"'

letter = """\
From: {mail_from}
To: {mail_to}
Subject: {subject}
Content-Type: {content_type};
Привет, {friend_name}! {my_name} приглашает тебя на сайт {website}!

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
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""" .format(website=website, my_name=my_name, friend_name=friend_name, mail_from=mail_from, mail_to=mail_to, subject=subject, content_type=content_type)

letter = letter.encode("UTF-8")

print(letter)

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(os.getenv('LOGIN'), os.getenv('PASSWORD'))
server.sendmail('laraxsmurf@yandex.ru', 'nikita.kozytenko@yandex.ru', letter)
server.quit()