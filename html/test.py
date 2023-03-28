import smtplib
from lxml import etree
from email.message import EmailMessage
msg=EmailMessage()
email_sender='15801657992@qq.com'
email_receiver='2196281600@qq.com'
msg['From']=email_sender
msg['to']=email_receiver
msg['Subjest']='test'
html=open("00.html","r",encoding="utf-8")
html = html.read()

msg.add_alternative(html,subtype='html')
server='smtp.qq.com'
port=465
passwd='hiyzinebopkgcijb'
with smtplib.SMTP_SSL(server,port) as server:
    server.login(email_sender,passwd)
    server.send_message(msg)
    server.quit()
