import smtplib , ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


server_gmail_smtp = "smtp.gmail.com"
port = 587
sender_email = "ENTER SENDER EMAIL"
recevier_email = "ENTER RECEVIERS EMAIL"
password = input("Enter Password for the sender email : ")


message = MIMEMultipart("alternative")
message["Subject"] = "Testing Mail1"
message["From"] = sender_email
message["To"] = recevier_email

text = """\
        This is Normal text

    """


html = """\
        <html>

        <body>
        <h1 align = "center" > HELLO,WORLD !!!</h1>
        <p> Write anything within the para </p>
        <h3>This is h3 TAG </h3>
        <img src = "https://picsum.photos/200/300"
        </body>

        </html>
    """

part1 = MIMEText(text,"plain")
part2 = MIMEText(html,"html")

message.attach(part1)
message.attach(part2)

context = ssl.create_default_context()
with smtplib.SMTP_SSL(server_gmail_smtp,465,context=context) as server:
    server.login(sender_email,password)
    server.sendmail(sender_email,recevier_email,message.as_string())

