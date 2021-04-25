import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = "AMAN SINGHAL"
email['to'] = 'amansinghal046@gmail.com'
email['subject'] = 'Hello AMAN'

email.set_content("Just Check")

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('amansinghal436@gmail.com','amansin892345')
    smtp.send_message(email)
    print("ALL GOOD")