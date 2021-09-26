
from ..database import db
from ..database.orms import *
from sqlalchemy.orm.exc import NoResultFound
from flask_restplus import reqparse
from datetime import datetime
from flask import request,url_for,render_template,make_response,jsonify,redirect,url_for
import random, json,os

def readGlobalFileHistoryData():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_uri = os.path.join(SITE_ROOT, 'file_details.json')
    with open(json_uri) as fo:
        return json.load(fo)

def getAllAlerts():
    all = readGlobalFileHistoryData()
    res = []
    for x in all:
        if x['latest']['version']['number_of_errors'] > 0:
            '''d = {}
            d['name'] = x['name']
            d['description'] = x['description']
            d['file_details'] = x['file_details']
            d['latest'] = x['latest']
            '''
            res.append(x)
    return res

def getAllFiles():
    all = readGlobalFileHistoryData()
    return all

def getSingleFile(file_name):
    all = readGlobalFileHistoryData()
    res = []
    for x in all:
        if x['name'] == file_name:
            res.append(x)

    return res
