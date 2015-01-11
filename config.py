# -*- coding: utf-8 -*-
import os
# Flask-WTF, forms
CSRF_ENABLED = True
SECRET_KEY = 'sfj0-\xda\xf5\xbf\x89\x81]%-t\t\x9a\x9d\x08\xaa]\x1a\xfe\xa4\xbe\xf8.&\xb3\xeb\xc1\xce\xee'

# OpenID providers
OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

# SQL-Alchemy
basedir = os.path.abspath(os.path.dirname(__file__))
# путь к файлу с нашей базой данных
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# это папка, где мы будем хранить файлы SQLAlchemy-migrate
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
