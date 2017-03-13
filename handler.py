import requirements
import json
from datetime import datetime
import pytz
import shutil
import os

# google drive
import httplib2

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

SCOPES = 'https://www.googleapis.com/auth/drive.file'

def create_drive(event, context):
    service = drive()
    service.files().create(
        body={
            'mimeType': 'application/vnd.google-apps.document',
            'name': document_name()
        }
    )
    return {
        'statusCode': 200,
        'body': document_name()
    }

def document_name():
    now = datetime.now(pytz.timezone('Asia/Tokyo'))
    return "{0}-{1}-{2}".format(now.year, now.month, now.day)

def drive():
    for env in os.environ:
        print env
    credential_path = '/tmp/drive-python-quickstart.json'
    with open(credential_path, 'w') as f:
        f.write(os.environ['credential'])
    store = Storage(credential_path)
    credentials = store.get()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)
    return service
