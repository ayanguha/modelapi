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


class edicategory(db.Model):
    edi_category_id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255))
    postedOn = db.Column(db.DateTime(), unique=False, nullable=False)
    updatedOn = db.Column(db.DateTime(), unique=False, nullable=False)


    def __init__(self,payload):
        self.edi_category_id = str(uuid.uuid4())
        self.name = payload['name']
        self.postedOn = datetime.now()
        self.updatedOn = datetime.now()

    @property
    def serialize(self):
       response_payload = {}
       response_payload['edi_category_id'] = self.edi_category_id
       response_payload['name'] = self.name
       return response_payload

class accrual_task_status_details(db.Model):
    accrual_task_status_details_id = db.Column(db.String(255), primary_key=True)
    status = db.Column(db.String(255))
    include = db.Column(db.String(20))
    postedOn = db.Column(db.DateTime(), unique=False, nullable=False)
    updatedOn = db.Column(db.DateTime(), unique=False, nullable=False)


    def __init__(self,payload):
        self.accrual_task_status_details_id = str(uuid.uuid4())
        self.status = payload['status']
        self.include = payload['include']
        self.postedOn = datetime.now()
        self.updatedOn = datetime.now()

    @property
    def serialize(self):
       response_payload = {}
       response_payload['accrual_task_status_details_id'] = self.accrual_task_status_details_id
       response_payload['status'] = self.status
       response_payload['include'] = self.include
       return response_payload

class edifile(db.Model):
    edifile_id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255))
    filelink = db.Column(db.String(255))
    postedOn = db.Column(db.DateTime(), unique=False, nullable=False)
    updatedOn = db.Column(db.DateTime(), unique=False, nullable=False)


    def __init__(self,payload):
        self.edifile_id = str(uuid.uuid4())
        self.name = payload['name']
        self.filelink = 'data/sample/file_example_XLSX_50.xlsx'
        self.postedOn = datetime.now()
        self.updatedOn = datetime.now()

    @property
    def serialize(self):
       response_payload = {}
       response_payload['edifile_id'] = self.edifile_id
       response_payload['name'] = self.name
       response_payload['filelink'] = self.filelink
       return response_payload


class supplier(db.Model):
    supplier_id = db.Column(db.String(255), primary_key=True)
    code = db.Column(db.String(255))
    name = db.Column(db.String(255))
    is_active = db.Column(db.String(20))
    postedOn = db.Column(db.DateTime(), unique=False, nullable=False)
    updatedOn = db.Column(db.DateTime(), unique=False, nullable=False)


    def __init__(self,payload):
        self.supplier_id = str(uuid.uuid4())
        self.code = payload['code']
        self.name = payload['name']
        self.is_active = payload['is_active']
        self.postedOn = datetime.now()
        self.updatedOn = datetime.now()

    @property
    def serialize(self):
       response_payload = {}
       response_payload['supplier_id'] = self.supplier_id
       response_payload['code'] = self.code
       response_payload['name'] = self.name
       response_payload['is_active'] = self.is_active
       return response_payload

class glaccount(db.Model):
    glaccount_id = db.Column(db.String(255), primary_key=True)
    code = db.Column(db.String(255))
    description = db.Column(db.String(255))
    financial_type = db.Column(db.String(255))
    is_active = db.Column(db.String(20))
    postedOn = db.Column(db.DateTime(), unique=False, nullable=False)
    updatedOn = db.Column(db.DateTime(), unique=False, nullable=False)


    def __init__(self,payload):
        self.glaccount_id = str(uuid.uuid4())
        self.code = payload['code']
        self.description = payload['description']
        self.financial_type = payload['financial_type']

        self.is_active = payload['is_active']
        self.postedOn = datetime.now()
        self.updatedOn = datetime.now()

    @property
    def serialize(self):
       response_payload = {}
       response_payload['glaccount_id'] = self.glaccount_id
       response_payload['code'] = self.code
       response_payload['description'] = self.description
       response_payload['financial_type'] = self.financial_type
       if self.is_active == 'Yes':
           response_payload['is_active'] = True
       if self.is_active == 'No':
           response_payload['is_active'] = False
       return response_payload

class transactionheader(db.Model):
    transactionheader_id = db.Column(db.String(255), primary_key=True)
    filename = db.Column(db.String(255))
    version = db.Column(db.String(255))
    header_text = db.Column(db.String(255))
    document_type = db.Column(db.String(255))
    calc_tax = db.Column(db.String(255))
    posting_date = db.Column(db.String(20))
    document_date = db.Column(db.String(20))
    document_reference = db.Column(db.String(255))
    currency = db.Column(db.String(20))
    vendor_code = db.Column(db.String(100))
    total_amount = db.Column(db.String(20))
    postedOn = db.Column(db.DateTime(), unique=False, nullable=False)
    updatedOn = db.Column(db.DateTime(), unique=False, nullable=False)


    def __init__(self,payload):
        self.transactionheader_id = str(uuid.uuid4())
        self.filename = payload['filename']
        self.version = payload['version']
        self.header_text = payload['header_text']
        self.document_type = payload['document_type']
        self.calc_tax = payload['calc_tax']
        self.posting_date = payload['posting_date']
        self.document_date = payload['document_date']
        self.document_reference = payload['document_reference']
        self.currency = payload['currency']
        self.vendor_code = payload['vendor_code']
        self.total_amount = payload['total_amount']

        self.postedOn = datetime.now()
        self.updatedOn = datetime.now()

    @property
    def serialize(self):
       response_payload = {}
       response_payload['transactionheader_id'] = self.transactionheader_id
       response_payload['filename'] = self.filename
       response_payload['version'] = self.version
       response_payload['header_text'] = self.header_text
       response_payload['document_type'] = self.document_type
       response_payload['calc_tax'] = self.calc_tax
       response_payload['posting_date'] = self.posting_date
       response_payload['document_date'] = self.document_date
       response_payload['document_reference'] = self.document_reference
       response_payload['currency'] = self.currency
       response_payload['vendor_code'] = self.vendor_code
       response_payload['total_amount'] = self.total_amount

       return response_payload

class transactiondetail(db.Model):
    transactiondetail_id = db.Column(db.String(255), primary_key=True)
    filename = db.Column(db.String(255))
    version = db.Column(db.String(255))
    line_number = db.Column(db.String(255))
    posting_key = db.Column(db.String(255))
    gl_account = db.Column(db.String(255))
    line_amount = db.Column(db.String(20))
    costcenter = db.Column(db.String(20))
    line_text = db.Column(db.String(1000))
    emplus_ref = db.Column(db.String(20))
    postedOn = db.Column(db.DateTime(), unique=False, nullable=False)
    updatedOn = db.Column(db.DateTime(), unique=False, nullable=False)


    def __init__(self,payload):
        self.transactiondetail_id = str(uuid.uuid4())
        self.filename = payload['filename']
        self.version = payload['version']
        self.line_number = payload['line_number']
        self.posting_key = payload['posting_key']
        self.gl_account = payload['gl_account']
        self.line_amount = payload['line_amount']
        self.costcenter = payload['costcenter']
        self.line_text = payload['line_text']
        self.emplus_ref = payload['emplus_ref']

        self.postedOn = datetime.now()
        self.updatedOn = datetime.now()

    @property
    def serialize(self):
       response_payload = {}
       response_payload['transactiondetail_id'] = self.transactiondetail_id
       response_payload['filename'] = self.filename
       response_payload['version'] = self.version
       response_payload['line_number'] = self.line_number
       response_payload['posting_key'] = self.posting_key
       response_payload['gl_account'] = self.gl_account
       response_payload['line_amount'] = self.line_amount
       response_payload['costcenter'] = self.costcenter
       response_payload['line_text'] = self.line_text
       response_payload['emplus_ref'] = self.emplus_ref

       return response_payload

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.user_id

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False
