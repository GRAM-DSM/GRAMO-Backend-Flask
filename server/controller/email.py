import smtplib
from email.mime.text import MIMEText

from server.config import EMAIL, EMAIL_PASSWORD


def send_email(title, content, adress):
    session = smtplib.SMTP(host='smtp.gmail.com', port=587)

    session.starttls()

    session.login(user=EMAIL, password=EMAIL_PASSWORD)

    mail = MIMEText(title)
    mail['Subject'] = content

    session.sendmail(from_addr=EMAIL, to_addrs=adress, msg=mail.as_string())

    session.quit()
