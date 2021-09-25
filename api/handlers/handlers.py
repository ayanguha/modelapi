from ..database import db
from ..database.orms import *
from sqlalchemy.orm.exc import NoResultFound
from flask_restplus import reqparse
from datetime import datetime
from flask import request,url_for,render_template,make_response,jsonify,redirect,url_for
import random, json,os

def safeCommit():
    try:
        db.session.commit()
    except:

        db.session.rollback()
        raise

def safeFlush():
    try:
        db.session.flush()
    except:

        db.session.rollback()
        raise

def modelExists(db,model):
    try:
        r = db.session.query(model).one()
        return True
    except:
        return False

def createAllModels(db):
    db.create_all()

def AccountResponseModification(list_account, params = {'expand': {'account': True}}):
    modified_account_response_list = []
    for a in list_account:
        ser = a.serialize
        ser['resource_url'] = url_for('api.v1_single_account_request',account_id=ser['id'], _external=True)
        if ser['parent_account_id'] :
            if params['expand']['account']:
                ser['account'] = getSingleAccount(ser['parent_account_id'])[0]
            else:
                ser['account'] = url_for('api.v1_single_account_request',account_id=ser['parent_account_id'], _external=True)
        modified_account_response_list.append(ser)
    return modified_account_response_list


def createAccount(request):
    createAllModels(db)
    payload = {}
    payload['name'] = request.json.get('name')
    payload['parent_account_id'] = request.json.get('parent_account_id')
    r = Account(payload)

    db.session.add(r)
    db.session.commit()
    return AccountResponseModification([r])


def getAllAccount():
    createAllModels(db)
    qryRes = Account\
                  .query\
                  .all()

    if qryRes:
        return AccountResponseModification(qryRes) #[i.serialize for i in qryRes]
    else:
        pass



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
            d = {}
            d['name'] = x['name']
            d['description'] = x['description']
            d['latest'] = x['latest']
            res.append(d)
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

def readGlobalEDICategoryData():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_uri = os.path.join(SITE_ROOT, 'edi_category.json')
    with open(json_uri) as fo:
        return json.load(fo)

def writeGlobalEDICategoryData(d):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_uri = os.path.join(SITE_ROOT, 'edi_category.json')
    with open(json_uri,'w') as fo:
        return json.dump(d,fo, indent=4)

def getAllEdiCategory():
    return readGlobalEDICategoryData()

def addEdiCategory(name):
    edi_category_global = readGlobalEDICategoryData()
    edi_category_global.append({'name': name, 'edi_category_id': random.randint(1,10000)})
    writeGlobalEDICategoryData(edi_category_global)
    return readGlobalEDICategoryData()

def updateEdiCategory(edi_category_id,name):
    print("edi_category_id:" + str(edi_category_id) + "  Name:" + name)
    edi_category_local = []
    edi_category_global = readGlobalEDICategoryData()
    for ec in edi_category_global:
        if ec['edi_category_id'] == int(edi_category_id.strip()):
            ec['name'] = name
    print("-----------------------------------")
    print(edi_category_global)
    print("-----------------------------------")
    writeGlobalEDICategoryData(edi_category_global)
    return readGlobalEDICategoryData()

def getEdiCategory(edi_category_id):
    edi_category_local = []
    edi_category_global = readGlobalEDICategoryData()
    for ec in edi_category_global:
        if  ec['edi_category_id'] == int(edi_category_id.strip()):
            edi_category_local.append(ec)
    return edi_category_local

def deleteEdiCategory(edi_category_id):
    edi_category_local = []
    edi_category_global = readGlobalEDICategoryData()
    for ec in edi_category_global:
        if ec['edi_category_id'] == int(edi_category_id.strip()):
            pass
        else:
            edi_category_local.append(ec)
    writeGlobalEDICategoryData(edi_category_local)
    return readGlobalEDICategoryData()

def getSingleAccount(account_id):
    qryRes = Account\
                  .query\
                  .filter_by(account_id = account_id)\
                  .all()

    if qryRes:
        return AccountResponseModification(qryRes) # return [i.serialize for i in qryRes]
    else:
        pass
