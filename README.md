# bestboyfriendbot
Это чат-бот в телеграме, имитирующий ласковые ответы от парня. 
Развернут на HEROKU, со стандартной базой postgresql. 
Поговорить с ним можно https://t.me/thebestboyfriendbot

Пока что он умеет не так много - лишь сохранять свой типаж и отвечать на текст или стикер текстом или стикером.

## Что в планах?
- Нормальное логирование
- Умение рассылать 'Доброе утро' и 'Спокойной ночи'
- Напоминать о годовщинах начала общения
- Уметь отличать осмысленный текст и какие-то стандартные ситуации ("Как дела?" и т.д.)
- Искать баги и фиксить их

## База данных
Простая как пять копеек
```
create table users_data (
	chat_id SERIAL PRIMARY key,
	create_date timestamp not null,
	boy_type int NOT NULL
);
```

## Contribute
Есть идея? Я рада любой помощи! Пиши https://t.me/Margo_ili_rita
Есть тестовый токен, чтобы не ломать бота
