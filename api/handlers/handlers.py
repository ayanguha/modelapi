from ..database import db
from ..database.orms import *
from sqlalchemy.orm.exc import NoResultFound
from flask_restplus import reqparse
from datetime import datetime
from flask import request,url_for,render_template,make_response,jsonify,redirect,url_for
import random, json,os



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



def getSingleAccount(account_id):
    qryRes = Account\
                  .query\
                  .filter_by(account_id = account_id)\
                  .all()

    if qryRes:
        return AccountResponseModification(qryRes) # return [i.serialize for i in qryRes]
    else:
        pass
