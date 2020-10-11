#!/usr/bin/python3
import base64
import smtplib
import traceback
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# 邮件发送
def send_mail(mail_host, from_user, to_users, password, mime_string):
    print("----------mail content----------------")
    print(mime_string)
    try:
        smtp_client = smtplib.SMTP()
        smtp_client.connect(mail_host, 25)
        smtp_client.ehlo()
        smtp_client.user = print_base64(from_user)
        smtp_client.password = print_base64(password)
        smtp_client.auth_login()
        # smtp_client.login(from_user, password)
        smtp_client.sendmail(from_user, to_users, mime_string)
        print("send successful")
    except smtplib.SMTPException:
        # print(sys.exc_info())
        traceback.print_exc()
        print("Error: send failed")


def print_base64(msg):
    encode = base64.b64encode(bytes(msg, encoding="utf-8")).decode()
    print("%s base64: %s" % (msg, encode))
    return encode


def deliver_simple_mail():
    message = MIMEText('mail content: test words ', 'plain', 'utf-8')
    message['From'] = Header('user1@lw.cn', 'utf-8')
    message['To'] = Header(",".join(['test@kiki052l.top']), 'utf-8')
    message['Subject'] = Header('simple mail demo', 'utf-8')
    send_mail(mail_host="lw.cn",
              from_user='user1@lw.cn',
              to_users=['test@kiki052l.top'],
              password='user1',
              mime_string=message.as_string())


def deliver_multipart_mail():
    ##邮件最外层
    msgRoot = MIMEMultipart('mixed')
    msgRoot['From'] = Header('user1@lw.cn', 'utf-8')
    msgRoot['To'] = Header(",".join(['test@kiki052l.top']), 'utf-8')
    msgRoot['Subject'] = Header('multipart mail demo', 'utf-8')
    msgRelated = MIMEMultipart('related')
    msgAlternative = MIMEMultipart('alternative')
    msgText = MIMEText('mail content: test words ', 'plain', 'utf-8')

    mail_msg = """
    <html><p>mail content: test words</p>
    <p><img src="cid:image1"></p></html>
    """
    ## background-image:url(data:image/png;base64)

    msgHtml = MIMEText(mail_msg, 'html', 'utf-8')
    fp = open('smtp-mime.jpg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', '<image1>')

    msgAttachment = MIMEText(open('demo.txt', 'rb').read(), 'base64', 'utf-8')
    msgAttachment["Content-Type"] = 'application/octet-stream'
    msgAttachment["Content-Disposition"] = 'attachment; filename="demo.txt"'
    msgAlternative.attach(msgText)
    msgAlternative.attach(msgHtml)
    msgRelated.attach(msgImage)
    msgRelated.attach(msgAlternative)
    msgRoot.attach(msgRelated)
    msgRoot.attach(msgAttachment)

    send_mail(mail_host="lw.cn",
              from_user='user1@lw.cn',
              to_users=['test@kiki052l.top'],
              password='user1',
              mime_string=msgRoot.as_string())


if __name__ == "__main__":
    deliver_simple_mail()
    deliver_multipart_mail()
