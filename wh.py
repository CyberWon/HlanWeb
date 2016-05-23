#!/usr/bin/python
#coding:utf-8
from flask import Flask,render_template,request
from hw.WebHlan import *
from hw.User import *
from hw.HWADMIN import *
import hlan

app = Flask(__name__)
app.register_blueprint(web_hlan)
app.register_blueprint(user_personal)
app.register_blueprint(user_check)
app.register_blueprint(user_login)
app.register_blueprint(hw_admin_hlan)
app.register_blueprint(hw_admin_project)
app.register_blueprint(hw_admin)

@app.route('/')
def index():
    return '首页'

if __name__=='__main__':
    app.run(host='0.0.0.0', port=1995,debug=True)