import uuid
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def __str2datetime__(s):
    try:
        return datetime.strptime(s,'%Y-%m-%dT%H:%M:%S.%fZ')
    except:
        return datetime.strptime(s + 'T00:00:00.000Z','%Y-%m-%dT%H:%M:%S.%fZ')

def __datetime2str__(d):
    return datetime.strftime(d,'%Y-%m-%dT%H:%M:%S.%fZ').decode('utf-8', 'ignore')
def __stringifyArray__(arr):
    return ",".join(arr)
def __stringifyArrayStruct__(arr):
    return "|".join([",".join([i+'#'+str(k[i]) for i in k.keys()]) for k in arr])
def __DestringifyArray__(s):
    return s.split(',')
def __DestringifyArrayStruct__(s):
    try:
        arr = [dict([i.split('#') for i in k.split(",")]) for k in s.split('|')]
    except:
        arr = []
    return arr

class Account(db.Model):
    account_id = db.Column(db.String(255), primary_key=True)
    parent_account_id = db.Column(db.String(255))
    name = db.Column(db.String(255))
    is_diabled = db.Column(db.String(255))
    postedOn = db.Column(db.DateTime(), unique=False, nullable=False)
    updatedOn = db.Column(db.DateTime(), unique=False, nullable=False)


    def __init__(self,payload):
        self.account_id = str(uuid.uuid4())
        self.name = payload['name']
        self.parent_account_id = payload['parent_account_id']
        self.is_diabled = False
        self.postedOn = datetime.now()
        self.updatedOn = datetime.now()

    @property
    def serialize(self):
       response_payload = {}
       response_payload['id'] = self.account_id
       response_payload['parent_account_id'] = self.parent_account_id
       response_payload['name'] = self.name
       response_payload['is_diabled'] = self.is_diabled
       return response_payload

class Device(db.Model):
    account_id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    is_diabled = db.Column(db.String(255), unique=False, nullable=False)
    postedOn = db.Column(db.DateTime(), unique=False, nullable=False)
    updatedOn = db.Column(db.DateTime(), unique=False, nullable=False)


    def __init__(self,payload):
        self.account_id = str(uuid.uuid4())
        self.name = payload['name']
        self.is_diabled = False
        self.postedOn = datetime.now()
        self.updatedOn = datetime.now()

    @property
    def serialize(self):
       return {'_id': self.account_id,
               'account_id': self.account_id,
               'name': self.name,
               'is_diabled': self.is_diabled

              }
