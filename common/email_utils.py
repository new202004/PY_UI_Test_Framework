# !/usr/bin/env python
# encoding: utf-8
# @author: new
# @file: mail_demo.py
# @time: 2020/5/10 9:17
# @desc
import os
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.mime.base import MIMEBase
from common.config_value import config
from common import zip_utils

current_path = os.path.dirname(__file__)
case_path = os.path.join(current_path, '../reports/禅道自动化测试报告-PYV1.5.rar')
report_path = os.path.join(current_path, case_path)


class EmailUtiles:
    def __init__(self, smtp_file=None):
        self.smtp_server = config.smtp_server  # 邮件服务器地址
        self.smtp_sender = config.smtp_sender  # 发送邮箱
        self.smtp_sender_password = config.smtp_sender_password  # 发送秘钥，通过qq邮箱--》设置--》开启POP3获取
        self.smtp_receiver = config.smtp_receiver  # 收件人
        self.smtp_cc = config.smtp_cc  # 抄送人
        self.smtp_subject = config.smtp_subject  # 标题
        self.smtp_body = config.smtp_body
        self.smtp_file = smtp_file  # 附件路径

    def main_contant(self):
        if self.smtp_file is not None:
            if self.smtp_file.split('.')[-1].__eq__('zip'):
                return self.__mail_zip_content()
        else:
            return self.__mail_text_content()

    def mail_content_by_zip(self):
        report_zip_path = self.smtp_file + '/../禅道自动化测试报告.zip'
        zip_utils.zip_dir(self.smtp_file, report_zip_path)
        self.smtp_file = report_zip_path # 压缩后改为压缩路径
        msg = self.main_contant()
        return msg

    def __mail_text_content(self):
        msg = MIMEText(self.smtp_body, 'html', 'utf-8')
        msg['from'] = self.smtp_sender
        msg['to'] = self.smtp_receiver
        msg['cc'] = self.smtp_cc
        msg['subject'] = self.smtp_subject
        return msg

    def __mail_zip_content(self):
        msg = MIMEMultipart()  # 发送带附件的邮件
        with open(self.smtp_file, 'rb') as f:
            mime = MIMEBase('zip', 'zip', filename=self.smtp_file.split('/')[-1])
            mime.add_header('Content-Disposition', 'attachment', filename=('gb2312', '', self.smtp_file.split('/')[-1]))
            mime.add_header('Contant-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            mime.set_payload(f.read())
            encoders.encode_base64(mime)
            msg.attach(mime)
        msg.attach(MIMEText(self.smtp_body, 'html', 'utf-8'))
        msg['from'] = self.smtp_sender
        msg['to'] = self.smtp_receiver
        msg['cc'] = self.smtp_cc
        msg['subject'] = self.smtp_subject
        return msg

    def send_mail(self):
        try:
            smtp = smtplib.SMTP()
            print(config.smtp_server)
            smtp.connect(self.smtp_server)
            smtp.login(user=self.smtp_sender, password=self.smtp_sender_password)
        except:
            smtp = smtplib.SMTP_SSL()
            smtp.login(user=self.smtp_sender, password=self.smtp_sender_password)
        mail_content = self.main_contant()
        try:
            smtp.sendmail(self.smtp_sender, self.smtp_receiver.split(',')+self.smtp_cc.split(','), mail_content.as_string())
        except Exception as e:
            print('发送失败')
        smtp.quit()

    def zip_send_email(self):
        try:
            smtp = smtplib.SMTP()
            print(config.smtp_server)
            smtp.connect(self.smtp_server)
            smtp.login(user=self.smtp_sender, password=self.smtp_sender_password)
        except:
            smtp = smtplib.SMTP_SSL()
            smtp.login(user=self.smtp_sender, password=self.smtp_sender_password)
        mail_content = self.mail_content_by_zip()
        try:
            smtp.sendmail(self.smtp_sender, self.smtp_receiver.split(',') + self.smtp_cc.split(','),
                          mail_content.as_string())
        except Exception as e:
            print('发送失败')
        smtp.quit()


if __name__ == '__main__':
    EmailUtiles().send_mail()