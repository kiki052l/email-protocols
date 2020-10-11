#!/usr/bin/python3
import poplib
from email.parser import Parser


def pull_mail():
    server = poplib.POP3('lw.cn', 110)
    server.user('test@kiki052l.top')
    server.pass_('test')
    print('Message: %s. Size: %s' % server.stat())
    resp, mails, objects = server.list()
    index = len(mails)
    print('user mail count=%d' % index)
    ##读取对应编号的邮件内容
    resp, lines, octets = server.retr(1)
    lists = []
    for e in lines:
        lists.append(e.decode())
    msg_content = '\r\n'.join(lists)
    msg = Parser().parsestr(msg_content)
    print(msg)
    server.dele(1)
    print('after delete Message: %s. Size: %s' % server.stat())
    server.quit()


if __name__ == "__main__":
    pull_mail()
