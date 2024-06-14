import random
import smtplib
import string
from email.mime.text import MIMEText

from config import settings

_from_addr = settings.EMAIL.get("ADDR")
_pwd = settings.EMAIL.get("PWD")
smtp_server = settings.EMAIL.get("SMTP_SERVER")


def generate_code():
    return "".join(random.choices(string.digits, 6))


def generate_email(to_addr) -> str:
    code = generate_code()
    head = "邮箱验证码"
    """标题"""
    text = f"您的验证码{code}，该验证码5分钟内有效，请勿泄漏于他人！"
    """正文"""
    send(to_addr, head, text)
    return code


def send(_to_addr, subject, content):
    msg = MIMEText(content, "plain", "utf-8")
    msg["From"] = _from_addr
    msg["To"] = _to_addr
    msg["Subject"] = subject

    server = smtplib.SMTP_SSL(smtp_server, 465)
    server.login(_from_addr, _pwd)
    server.sendmail(_from_addr, _to_addr, msg.as_string())
    server.quit()


if __name__ == "__main__":
    email1 = generate_email()
    print(email1)
