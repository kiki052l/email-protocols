## RFC INDEX

| RFCs        	    | 时间          | 标题                                                       | 内容                                                   |
| ----------------- | --------------- | ------------------------------------------------------------ | -------------------------------------------------------- |
| rfc821.pdf<div style="width: 80pt">  	 | <div style="width: 100pt">August 1982     | Simple Mail Transfer Protocol                                | 邮件传输协议                                       |
| rfc822.pdf  	 | August 13, 1982 | STANDARD FOR THE FORMAT OFARPA INTERNET TEXT MESSAGES       | 邮件内容标准                                       |
| rfc1425.pdf 	 | February 1993   | SMTP Service Extensions                                      | 对RFC821的扩展                |
| rfc1426.pdf 	 | February 1993   | SMTP Service Extensionfor 8bit-MIMEtransport                | 8bitmime传输标准                                     |
| rfc1939.pdf 	 | May 1996        | Post Office Protocol - Version 3                             | POP3标准                                               |
| rfc2045.pdf 	 | November 1996   | MIME Part One:Format of Internet Message Bodies              | MIME标准-消息体格式                               |
| rfc2046.pdf 	 | November 1996   | MIME Part Two:Media Types                                    | MIME标准-消息媒体类型                            |
| rfc2047.pdf 	 | November 1996   | MIME Part Three:Message Header Extensions for Non-ASCII Text | MIME标准-非ascii码消息头扩展                   |
| rfc2048.pdf 	 | November 1996   | MIME Part Four:Registration Procedures                       | MIME标准-注册流程media type, content-transfer-encodings |
| rfc2049.pdf 	 | November 1996   | MIME Part Five:Conformance Criteria and Examples             | MIME标准-一致性标准消息,格式参考           |
| rfc3501.pdf 	 | March 2003      | INTERNET MESSAGE ACCESS PROTOCOL - VERSION 4rev1             | IMAP4邮件访问标准         


## 电子邮件系统搭建

### james邮件系统

>  Apache James 简称 James, 是 Java Apache Mail Enterprise Server的缩写。James 是100%基于Java的电子邮件服务器。它是一种独立的邮件服务器，并提供了一个完整的电子邮件解决方案

##### 拉取james docker镜像

```
docker pull linagora/james-jpa-sample
```
##### 启动james服务

```
docker run --hostname mail.lw.cn -w /root -v /home/ubuntu/james_mail/conf:/root/tmp -p "25:25" -p "110:110" -p "143:143" -p "465:465"  -p "993:993" --name email -d linagora/james-jpa-sample

```
##### 查看james服务端命令

```
docker exec email java -jar /root/james-cli.jar
```
##### 添加domain

```
sudo docker exec email java -jar /root/james-cli.jar AddDomain kiki052l.top
sudo docker exec email java -jar /root/james-cli.jar AddDomain lw.cn
```
##### 添加用户

```
sudo docker exec email java -jar /root/james-cli.jar AddUser test@kiki052l.top test
sudo docker exec email java -jar /root/james-cli.jar AddUser test01@kiki052l.top test
sudo docker exec email java -jar /root/james-cli.jar AddUser user1@lw.cn user1
sudo docker exec email java -jar /root/james-cli.jar AddUser user2@kiki052l.top user2
```
##### 查看已添加domain&用户

```
sudo docker exec email java -jar /root/james-cli.jar  ListDomains
sudo docker exec email java -jar /root/james-cli.jar  ListUsers
```