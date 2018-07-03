from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from email.mime.text import MIMEText
import base64
import sys

def create_message(subject, text) :
    message = MIMEText(text);
    message['to'] = 'wayne.ngan@gmail.com'
    message['from'] = 'me'
    message['subject'] = subject
    return { 'raw': base64.urlsafe_b64encode(message.as_string()) }
    

def send_message(service, message) :
    service.users().messages().send(userId='me', body=message).execute()
#    print('Message Id: ' + message['id'])
    return message

def send_gmail(subject_text, msg_text) :
    # Setup the Gmail API
    SCOPES = 'https://www.googleapis.com/auth/gmail.send'
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))
    
    # Call the Gmail API
    msg = create_message(subject_text, msg_text)
    rc = send_message(service, msg)

