import smtplib
from email.message import EmailMessage
msg=EmailMessage()
email_sender='15801657992@qq.com'
email_receiver='2196281600@qq.com'
msg['From']=email_sender
msg['to']=email_receiver
msg['Subjest']='test'
msg.set_content('this is test')
server='smtp.qq.com'
port=465
passwd='' #自己打开邮箱--设置 --账户--开启服务--IMAP/SMTP 复制 授权码
with smtplib.SMTP_SSL(server,port) as server:
    server.login(email_sender,passwd)
    server.send_message(msg)
    server.quit()
