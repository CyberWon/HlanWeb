#!/usr/bin/python
#coding:utf-8
from flask import Blueprint, render_template,request
user_personal=Blueprint('user_personal',__name__,template_folder='/templates')
user_login=Blueprint('user_login',__name__,template_folder='/templates')
user_check=Blueprint('user_check',__name__,template_folder='/templates')
@user_personal.route('/User/Personal/<g>')
def UserPersonal(g):
    from hw import Personal
    if g=='Face':
        res=Personal.Face()
    elif g=='Profile':
        res=Personal.Profile()
    else:
        res='没有这个页面。'
    return res
@user_login.route('/User/Login')
def UserLogin():  
    return render_template('User/login.html')

@user_check.route('/User/Check',methods=['GET', 'POST'])
def UserCheck():
    from hw import Verity
    user_act=request.args.get('act')
    if user_act == 'login':
        user_name=request.form['user']
        user_passwd=request.form['passwd']
        if Verity.Login(user_name, user_passwd):
            return '登陆成功'
        else:
            return '登陆失败'
    return render_template('User/login.html')
