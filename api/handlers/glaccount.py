from ..database import db
from ..database.orms import *
from sqlalchemy.orm.exc import NoResultFound
from flask_restplus import reqparse
from datetime import datetime
from flask import request,url_for,render_template,make_response,jsonify,redirect,url_for
import random, json,os
from .util import *


def getAllGlaccount():
    qryRes = glaccount.query.all()
    return [i.serialize for i in qryRes]

def addGlaccount(code,description,financial_type,is_active):
    payload = {}
    payload['code'] = code
    payload['description'] = description
    payload['financial_type'] = financial_type
    if is_active:
        payload['is_active'] = 'Yes'
    else:
        payload['is_active'] = 'No'
    r = glaccount(payload)

    db.session.add(r)
    safeFlush()
    safeCommit()
    return getAllGlaccount()

def updateGlaccount(glaccount_id,code,description,financial_type,is_active):
    qryRes = glaccount.query.filter_by(glaccount_id = glaccount_id).all()
    r = qryRes[0]
    r.code = code
    r.description = description
    r.financial_type = financial_type
    if is_active:
        r.is_active = 'Yes'
    else:
        r.is_active = 'No'
    
    safeFlush()
    safeCommit()
    return getAllGlaccount()

def getGlaccount(glaccount_id):
    qryRes = glaccount.query.filter_by(glaccount_id = glaccount_id).all()

    if qryRes:
        return  [i.serialize for i in qryRes]
    else:
        pass

def deleteGlaccount(glaccount_id):
    qryRes = glaccount.query.filter_by(glaccount_id = glaccount_id).all()
    r = qryRes[0]

    db.session.delete(r)
    safeFlush()
    safeCommit()
    return getAllGlaccount()
