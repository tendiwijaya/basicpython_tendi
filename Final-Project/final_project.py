import smtplib

def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails


from string import Template

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

names, emails = get_contacts('receiver_list.txt')

emailAnda = input("Input Email Gmail Anda :")
emailpassword = input("Input Password Email Anda :")

for name, email in zip(names, emails):
    msg = MIMEMultipart()       # create a message

    # add in the actual person name to the message template
    fromaddr = emailAnda
    toaddr = email

    # setup the parameters of the message
    msg['From']=fromaddr
    msg['To']=email
    msg['Subject']="Final Project Python - Send Email"

    # add in the message body
    body = "Ini adalah final project Python Indonesia.ai mengenai sending email."
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, emailpassword)
    text = msg.as_string()

    server.sendmail(fromaddr, toaddr, text)
    server.quit()

    # send the message via the server set up earlier.
    # s.send_message(msg)
    del msg


# Referensi 1 : https://realpython.com/python-send-email/
# Referensi 2 : https://www.freecodecamp.org/news/send-emails-using-code-4fcea9df63f/
# Referensi 3 : https://www.pythonindo.com/cara-mengirim-email-menggunakan-python/