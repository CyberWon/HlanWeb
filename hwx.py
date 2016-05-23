#coding:utf-8
from ext.WXBizMsgCrypt import WXBizMsgCrypt
import xml.etree.cElementTree  as ET
from flask import Flask, request
from ext.conf import requireWX,readWxHTML
from hwx.WxMsg import wxMsgNew
from hwx.WxMain import hlan_main
wx_conf=requireWX()
app = Flask(__name__)
@app.route('/m/<g>')
def web_main(g):
    res=readWxHTML(g)
    return res
@app.route('/wechat', methods=['GET', 'POST'])
def wechat():
    global wx_conf
    sToken = wx_conf['token']
    sEncodingAESKey = wx_conf['aes_key']
    sCorpID = wx_conf['appid']
    try:
        wxcpt=WXBizMsgCrypt(sToken,sEncodingAESKey,sCorpID)
    except Exception as e:
        print(e)
    sVerifyMsgSig=request.args.get('msg_signature')
    sVerifyTimeStamp=request.args.get('timestamp')
    sVerifyNonce=request.args.get('nonce')
    if request.method == 'GET':
        sVerifyEchoStr=request.args.get('echostr')
        try:
            ret,sEchoStr=wxcpt.VerifyURL(sVerifyMsgSig, sVerifyTimeStamp,sVerifyNonce,sVerifyEchoStr)
            if(ret!=0):
                print("ERR: VerifyURL ret:%s" % ret)
        except Exception as e:
            print(e)
        return sEchoStr
    ret,sMsg=wxcpt.DecryptMsg(request.data, sVerifyMsgSig, sVerifyTimeStamp, sVerifyNonce)
    if( ret!=0 ):
        print("ERR: DecryptMsg ret:%s "% ret)
    xml_tree = ET.fromstring(sMsg)
    wx_to_user = xml_tree.find("ToUserName").text
    wx_from_user = xml_tree.find("FromUserName").text
    wx_create_time = xml_tree.find("CreateTime").text
    wx_msg_type = xml_tree.find("MsgType").text
    wx_appid = xml_tree.find("AgentID").text
    wx_content = xml_tree.find("Content").text
    wx_msg_id = xml_tree.find("MsgId").text
#     sRespData=wxMsgText(wx_to_user, wx_from_user, wx_create_time, wx_msg_type, wx_content, wx_msg_id, wx_appid)
    if wx_msg_type=='text':
        msg_content=hlan_main(wx_content)
    wx_url='%sm/%s'  % (wx_conf['url'],wx_content)
    sRespData=wxMsgNew(wx_to_user, wx_from_user, wx_create_time,wx_content,msg_content,wx_url)
    ret,sEncryptMsg=wxcpt.EncryptMsg(sRespData, sVerifyNonce, sVerifyTimeStamp)
    if( ret!=0 ):
        print("ERR: DecryptMsg ret:%s "% ret)
    return sEncryptMsg

if __name__=='__main__':
    app.run('0.0.0.0', 917, debug=True)