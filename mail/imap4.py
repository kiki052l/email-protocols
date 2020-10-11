import imaplib


def tech_mail():
    email_address = "test@kiki052l.top"
    email_password = "test"
    imap_server_host = "lw.cn"
    imap_server_port = 993
    try:
        email_server = imaplib.IMAP4_SSL(host=imap_server_host, port=imap_server_port)
        email_server.login(email_address, email_password)
    except:
        print("IMAP4 access error")
        exit(1)
    email_server.select(mailbox='INBOX')
    email_count = len(email_server.search(None, 'ALL')[1][0].split())
    ##读取最后一封邮件，只查看邮件头
    typ, email_content = email_server.fetch(f'{email_count}'.encode(), '(RFC822.HEADER)')
    email_content = email_content[0][1].decode()
    print(email_content)
    email_server.close()
    email_server.logout()


if __name__ == "__main__":
    tech_mail()
