#!/usr/bin/python
#coding:utf-8
def out_project_list(dick_pj):
    res='''{% extends "hproject/index.html" %}
{% block content %}'''
    res+=out_project(dick_pj)
    res+='{% endblock %}'
    return res
def out_project(dick_pj):
    res=''
    for (k,v) in dick_pj.items():
        res+='''<li><a href="#" ref="%s">%s</a></li>\n''' %(k,k)
        if type(v)==dict:
            res+="<ul>"
            for (k1,v1) in v.items():
                res+='''<li><a href="#" ref="%s">%s</a></li>\n''' %(k1,k1)
                res+="<ul>"
                if type(v1)==dict:
                    res+=out_project(v1)
                elif type(v1)==str:
                    res+='''<li><a href="#" ref="%s">%s</a></li>\n''' %(v1,v1)
                elif type(v1)==list:
                    print v1
                else:
                    res+='''<li><a id=name ref="%s">%s</a></li>\n''' % (v1.encode("utf-8"),v1.encode("utf-8"))
                res+="</ul>"
            res+="</ul>"           
        else:
            res+="<ul>"
            if type(v)==list:
                for i in v:
                    res+='''<li><a href="#" ref="%s">%s</a></li>\n''' %(i,i)
            else:
                res+='''<li><a href="#" ref="%s">%s</a></li>\n''' %(v,v)
            res+="</ul>"
    return res 