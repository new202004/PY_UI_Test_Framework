# !/usr/bin/env python
# encoding: utf-8
# @author: new
# @file: mail_demo.py
# @time: 2020/5/10 9:17
# @desc
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os
from email.mime.base import MIMEBase

current_path = os.path.dirname(__file__)
case_path = os.path.join(current_path, '../reports/禅道自动化测试报告-PYV1.5.rar')
report_path = os.path.join(current_path, case_path)

smtp_server = 'smtp.qq.com'  # 邮件服务器地址
smtp_sender = '479262985@qq.com'  # 发送邮箱
smtp_sender_password = 'axjfqbsfefjhbjgb'  # 发送秘钥，通过qq邮箱--》设置--》开启POP3获取
smtp_receiver = '1595232458@qq.com'  # 收件人
smtp_cc = '479262985@qq.com'  # 抄送人
smtp_subject = 'UI自动化测试报告'  # 标题
smtp_body = '来自new的自动化测试报告邮件正文'  # 正文
smtp_file = report_path  # 附件路径

msg = MIMEText(smtp_body, 'html', 'utf-8')  # 发送只有正文的邮件
msg['from'] = smtp_sender
msg['to'] = smtp_receiver
msg['cc'] = smtp_cc
msg['subject'] = smtp_subject

# msg = MIMEMultipart()  # 发送带附件的邮件
# with open(smtp_file, 'rb') as f:
#     mime = MIMEBase('zip', 'zip')


smtp = smtplib.SMTP()
smtp.connect(smtp_server)
smtp.login(user=smtp_sender, password=smtp_sender_password)
smtp.sendmail(smtp_sender, smtp_receiver.split(',')+smtp_cc.split(','), msg.as_string())
