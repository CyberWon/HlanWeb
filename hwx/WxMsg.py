#!/usr/bin/python
#coding:utf-8
def wxMsgNew(wx_to_user,wx_from_user,wx_create_time,title,wx_content,wx_url):
    if wx_content=='生成失败了':
        wx_url=''
    sRespData='''<xml>
   <ToUserName><![CDATA[%s]]></ToUserName>
   <FromUserName><![CDATA[%s]]></FromUserName>
   <CreateTime>%s</CreateTime>
   <MsgType><![CDATA[%s]]></MsgType>
   <ArticleCount>1</ArticleCount>
   <Articles>
       <item>
           <Title><![CDATA[%s]]></Title> 
           <Description><![CDATA[%s]]></Description>
           <PicUrl><![CDATA[%s]]></PicUrl>
           <Url><![CDATA[%s]]></Url>
       </item>
   </Articles>
</xml>''' %(wx_to_user,
                wx_from_user,
                wx_create_time,
                'news',
                title,
                wx_content,
                '',
                wx_url
                ) 
    return sRespData
def wxMsgText(wx_to_user,wx_from_user,wx_create_time,wx_msg_type,wx_content,wx_msg_id,wx_appid):
    sRespData = '''<xml>
    <ToUserName><![CDATA[%s]]></ToUserName>
    <FromUserName><![CDATA[%s]]>
    </FromUserName><CreateTime>%s</CreateTime>
    <MsgType><![CDATA[%s]]></MsgType>
    <Content><![CDATA[%s]]></Content>
    <MsgId>%s</MsgId>
    <AgentID>%s</AgentID>
    </xml>''' %(wx_to_user,
                wx_from_user,
                wx_create_time,
                wx_msg_type,
                wx_content,
                wx_msg_id,
                wx_appid
                )
    return sRespData