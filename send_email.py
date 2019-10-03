import smtplib
import config


def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        # server.ehlo()
        server.starttls()
        server.login(config.EMAIL_FROM_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n {}'.format(subject, msg)
        server.sendmail(config.EMAIL_FROM_ADDRESS, config.EMAIL_TO_ADDRESS, message)
        server.quit()
        print('Success! Email send!')
    except:
        print('Email faild to send.')


#subject = "test subject"
#msg = "Hello there! How R U today?"
#
#send_email(subject, msg)
