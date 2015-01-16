# -*- coding: utf-8 -*-
import os
# Flask-WTF, forms
CSRF_ENABLED = True
SECRET_KEY = 'sfj0-\xda\xf5\xbf\x89\x81]%-t\t\x9a\x9d\x08\xaa]\x1a\xfe\xa4\xbe\xf8.&\xb3\xeb\xc1\xce\xee'

# OpenID providers
OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yandex', 'url': 'http://openid.yandex.ru/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'},
]

# Пагинация
POSTS_PER_PAGE = 3
# SQL-Alchemy
basedir = os.path.abspath(os.path.dirname(__file__))
# путь к файлу с нашей базой данных
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# mysql для тестов
# SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://flaskapp:superpassword@localhost/app?charset=utf8&use_unicode=0'
# это папка, где мы будем хранить файлы SQLAlchemy-migrate
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# Настройки для отправки почты администраторам
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

# administrator list
ADMINS = ['postrg@gmail.com']