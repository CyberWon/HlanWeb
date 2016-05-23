#!/usr/bin/python
#coding:utf-8
from flask import Blueprint
import hlan,json
web_hlan=Blueprint('web_hlan',__name__,template_folder='/templates')
@web_hlan.route('/Admin/Hlan/<g>')
def AdminHlanG(g):
    from ext.conf import hlan_table_footer,hlan_table_header
    li=['hlan.py',g]
    try:
        try:
            mod_json=hlan.main(li)
        except Exception as e:
            return e
        res=json.loads(mod_json)
        Res=hlan_table_header
        for k in res:
            res_value=res[k]['value']
            Res_Status=res[k]['status']
            Res_Value=''
            for i in res_value:
                Res_Value+='%s\n'% res_value[i]
            Res+='''<tr class="footable-even footable-detail-show" style="display: table-row;">
    <td>%s</td>
    <td><pre>%s
    </pre>
    </td>
    <td><a href="#"><i class="fa fa-check text-navy"></i>%s</a></td>
    </tr>
            '''%(k.encode('utf-8'),Res_Value.encode('utf-8'),Res_Status.encode('utf-8'))
        Res+=hlan_table_footer
        return Res
    except Exception as e:
        return e.message