#!/usr/bin/env python3

import cgi
import cgitb

cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect
import os
import secret
from http.cookies import SimpleCookie

# Create instance of FieldStorage
form = cgi.FieldStorage()
username = form.getfirst('username')
password = form.getfirst('password')

form_ok = username == secret.username and password == secret.password

if not username and not password:
    print(login_page())
elif form_ok:
    print("Set-Cookie: username={};".format(username))
    print("Set-Cookie: password={};".format(password))
    print(secret_page(username, password))
else:
    print(after_login_incorrect())

cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
username = cookie.get("username")
password = cookie.get("password")

if cookie.get("username") and cookie.get("password"):
    print(secret_page(username.value, password.value))
else:
    print(login_page())