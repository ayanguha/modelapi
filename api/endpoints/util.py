
from openpyxl import load_workbook
from datetime import datetime
from tempfile import NamedTemporaryFile
import boto3
import botocore

import json
import boto3
import os

from werkzeug.utils import secure_filename

S3_BUCKET =  'modelapi'
S3_KEY = os.environ['S3_KEY']
S3_SECRET = os.environ['S3_SECRET']


def getPresignedURLByFile(srcfilename, contenttype,destfolder):
    session = boto3.session.Session(aws_access_key_id=S3_KEY,
                                    aws_secret_access_key=S3_SECRET)
    s3 = session.resource('s3')
    srcfilename = secure_filename(srcfilename)
    destFileName = destfolder + "/" + srcfilename

    psurl = s3.meta.client.generate_presigned_url(
    ClientMethod='put_object',
    Params={'Bucket': S3_BUCKET,
            'Key': destFileName,
            "ContentType": contenttype,
            "ContentDisposition": "attachment"
            }
           )
    dwurl = destFileName #getS3Link(destFileName)

    return (psurl,dwurl)

def download_file(key):
    try:
        file = NamedTemporaryFile(suffix = '.xlsx', delete=False)
        session = boto3.session.Session(aws_access_key_id=S3_KEY,
                                        aws_secret_access_key=S3_SECRET)
        s3 = session.resource('s3')
        s3.Bucket(S3_BUCKET).download_file(key, file.name)
        return file.name
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            return None
        else:
            raise
    else:
        raise

def formatdate(s):
    return datetime.strptime(s, '%d.%m.%y').strftime('%m/%d/%Y')

def get_val(r):
    o = []
    for k in r:
        o.append(k.value)
    return o


def standardize_headers(headers):

    o = []
    for k in headers:
        if k:
            h = k.replace(' ','_').replace('/','_').lower()
            print("k:" + str(k) + "  h:" + str(h))
            o.append(h)


    return o

def parse_xls(filename):
    workbook = load_workbook(filename=filename)

    sheet = workbook.active

    data = []
    details = []
    for row in sheet.rows:

        if row[0].row == 1:

            headers = standardize_headers(get_val(row))
        else:
            details.append(get_val(row))


    for detail in details:
        record = {}
        zipped = zip(headers,detail)
        for z in zipped:
            record[z[0]] = str(z[1])
        data.append(record)


    return data
