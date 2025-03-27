import smptlib
from email.mine.text import MIMEText # Import MIMEText module is a class that represents the message body
from email.mime.multipart import MIMEMultipart # Import MIMEMultipart module is a class that represents the message itself




import os
def send_mail(workflow_name, repo_name):
    #Email details
    sender_email=os.getenv('SENDER_EMAIL')
    sender_password=os.getenv('SENDER_PASSWORD')
    receiver_email=os.getenv('RECEIVER_EMAIL')

    # Email message
    subject= f"Workflow {workflow_name} has failed for repo {repo_name}"
    body= f"Hi, \n\nThe workflow {workflow_name} has failed for repo {repo_name}. please check the logs for more details.\n\nThanks \nRun_ID :{workflow_run_id}"

    msg= MIMEMultipart()

    msg['From']= sender_email
    msg['To']=receiver_email
    msg['subject']=subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smptplib.SMTP('smptp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text=msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print('Email sent successfully')
    except Exception as e:
        print(f"Error: {e}")
        print('Email not sent')

send_mail(os.getenv('WORKFLOW_NAME'), os.getenv('REPO_NAME'), os.getenv('WORKFLOW_RUN_ID'))



