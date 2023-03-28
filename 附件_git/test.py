import smtplib
from lxml import etree
import imghdr
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
msg=MIMEMultipart()
email_sender='15801657992@qq.com'
email_receiver='2196281600@qq.com'
msg['From']=email_sender
msg['to']=email_receiver
msg['Subjest']='test'
imageFile='test.jpg'
image=MIMEApplication(open(imageFile, 'rb').read())
image.add_header('Content-Disposition', 'attachment', filename=imageFile)
msg.attach(image)
pdfFile='mathtype.pdf'
pdf=MIMEApplication(open(pdfFile, 'rb').read())
pdf.add_header('Content-Disposition', 'attachment', filename=pdfFile)
msg.attach(pdf)
docFile='mathtype.docx'
doc=MIMEApplication(open(pdfFile, 'rb').read())
doc.add_header('Content-Disposition', 'attachment', filename=docFile)
msg.attach(doc)

server='smtp.qq.com'
port=465
passwd='' #自己打开邮箱--设置 --账户--开启服务--IMAP/SMTP 复制 授权码
with smtplib.SMTP_SSL(server,port) as server:
    server.login(email_sender,passwd)
    server.send_message(msg)
    server.quit()
