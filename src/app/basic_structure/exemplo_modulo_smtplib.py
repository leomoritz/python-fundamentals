# coding=utf-8
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def create_message(from_email, to_email, subject, text_message):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(text_message, 'plain'))
    return msg


def create_server():
    return smtplib.SMTP('localhost', 1025)


def login(email, password, use_tls=True):
    """
    Realiza o login no servidor de e-mail. Apenas para servidores que exigem autenticação.
    Por padrão é utilizado o TLS (Transport Layer Security) para fornecer segurança na comunicação.
    :param email: e-mail do remetente
    :param password: senha do remetente
    :param use_tls: caso seja True, utiliza o TLS para comunicação segura
    """
    global server
    if use_tls:
        server.ehlo()
        server.starttls()
        server.ehlo()
    server.login(email, password)


def send_email(msg):
    global server
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    print("Email sent successfully")


message = create_message("from_python@gmail.com", "to_python@outlook.com", "Hello", "Hello World from Python")
server = create_server()
send_email(message)
server.quit()
