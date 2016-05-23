#!/usr/bin/python
#coding:utf-8
from flask import Blueprint, render_template,request
hw_admin=Blueprint('hw_admin',__name__,template_folder='/templates')
hw_admin_project=Blueprint('hw_admin_project',__name__,template_folder='/templates')
hw_admin_hlan=Blueprint('hw_admin_hlan',__name__,template_folder='/templates')
@hw_admin.route('/Admin/',methods=['GET', 'POST'])
def Admin():
    return render_template('Admin/index.html')

@hw_admin_project.route('/Admin/Project/<g>')
def AdminProject(g):
    return g
@hw_admin_hlan.route('/Admin/Hlan')
def AdminHlan():
    return render_template('Admin/webhlan.html')
