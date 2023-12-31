#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_httpauth import HTTPBasicAuth

from src.app.db import db
from src.app.services.AuthService import verify_password
from src.app.services.UserService import UserService

app = Flask(__name__)
app.config.from_object('src.app.config')

# Initialize database config
db.init_app(app)

#  This allows us to use the server without having it online
with app.app_context():
    db.create_all()

auth = HTTPBasicAuth()
auth.verify_password_callback = verify_password

with app.app_context():
    try:
        UserService().create_user("ytm@ytm.com", "changeit")
    except ValueError:
        pass
