import smtplib
from email.mime.text import MIMEText

title = "test"
receiver="dwkim8155@gmail.com"
def mails(content):
    smtp = smtplib.SMTP('smtp.gmail.com', 587)

    smtp.ehlo()

    smtp.starttls()

    smtp.login('qogywofhqht@gmail.com', 'iokw zaeu nbtd esgl')

    msg = MIMEText(content)
    msg['Subject'] = title

    smtp.sendmail('qogywofhqht@gmail.com', receiver, msg.as_string())

    smtp.quit()
    print("완료")