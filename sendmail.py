import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def send_email(name, email, message):
    date_time = datetime.now()
    d = date_time.strftime("%c")

    sender_email = "fluttersolutionsdev@gmail.com"
    receiver_email = "gandhimanan1@gmail.com"
    password = "rryyovewjnjjplaf"
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "New Client Website"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hello,
    How are you doing?
    Real Python has many great tutorials:
    www.realpython.com
   """
    html = """\
    <html>
      <body>
        <p>Hi Manan,<br>
           How are you?<br>
    I am {name}
    My email {email}
    {message}
    <br>
    Login Time: <b>{time}</b>
      </body>
    </html>
    """.format(time=d,name=name,email=email,message=message)
    
    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    msg.attach(part1)
    msg.attach(part2)
    
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()
    
if __name__ == "__main__":
    name = "rajesh"
    email = "123@gmail.com"
    message = "need an app"
    send_email(name, email, message)
