import smtplib
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders


def send_mail(send_from, send_to, subject,
              server="smtp.gmail.com", port=587, username='', password=''):
    """Compose and send email with provided info and attachments.

    Args:
        send_from (str): from name
        send_to (list[str]): to name(s)
        subject (str): message title
        message (str): message body
        files (list[str]): list of file paths to be attached to email
        server (str): mail server host name
        port (int): port number
        username (str): server auth username
        password (str): server auth password
        use_tls (bool): use TLS mode
    """
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    html = """\
<html>
    <body>
        <div style="background-color:#eee;padding:10px 20px;">
            <h2 style="font-family:Georgia, 'Times New Roman', Times, serif;color#454349;">ODBIERZ DARMOWEGO IPHONA</h2>
        </div>
        <div style="padding:20px 0px">
            <div style="height: 500px;width:400px">
                <img src="https://www.gsmmaniak.pl/wp-content/uploads/gsmmaniak/2021/09/Zrzut-ekranu-2021-09-14-o-19.41.09.jpg" style="height: 300px;">
                <div style="text-align:center;">
                    <h3>DARMOWY TELEFON!</h3>
                    <a href="http://192.168.1.31/">KLIKNIJ ABY PRZEJŚĆ NA STRONĘ Z DARMOWYMI IPHONAMI XIII!!!</a>
                </div>
            </div>
        </div>
    </body>
</html>
"""
    msg.attach(MIMEText(html, 'html'))
    
    smtp = smtplib.SMTP(server, port)
    smtp.connect(server,port)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(username, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()
    print("udalo sie")

adresaci = ['s180102@student.pg.edu.pl']
tytul = 'Wygrałeś iPhona!'
send_mail('eDziekanat',adresaci,tytul,'smtp.gmail.com',587,'helpdesk.pg.edu.pl@gmail.com','dzmaplwglxufzfqs')