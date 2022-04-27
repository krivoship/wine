# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

Необходимо скачать или склонировать репозиторий с проектом: https://github.com/krivoship/wine.

В файле `.env` должен лежать путь к файлу excel с информацией по напиткам.
```
DRINKS_INFO='Ваш путь к файлу с информацией по напиткам'
```
Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

Запустите сайт командой `python3 main.py`

Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
