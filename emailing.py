from email.message import EmailMessage
import imghdr
password = "ccug yybj hkhp ekjv"
user_email = "farazyamaan@gmail.com"
receiver_email = "farazyamaan@gmail.com"
import smtplib
def send_email(image_path):
    email_msg = EmailMessage()
    email_msg['Subject'] = ('Hello To Yamaan Faraz Course.')
    email_msg.set_content("Hello, And welcome!.")

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(user_email, password)
    gmail.sendmail(user_email, receiver_email, email_msg.as_string())
    gmail.quit()

if __name__ == '__main__':
    send_email(image_path="images/496.png")