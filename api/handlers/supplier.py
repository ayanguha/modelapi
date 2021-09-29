from ..database import db
from ..database.orms import *
from sqlalchemy.orm.exc import NoResultFound
from flask_restplus import reqparse
from datetime import datetime
from flask import request,url_for,render_template,make_response,jsonify,redirect,url_for
import random, json,os
from .util import *


def getAllSupplier():
    qryRes = supplier.query.all()
    return [i.serialize for i in qryRes]

def addSupplier(name,code,is_active):
    payload = {}
    payload['name'] = name
    payload['code'] = code
    payload['is_active'] = is_active
    r = supplier(payload)

    db.session.add(r)
    safeFlush()
    safeCommit()
    return getAllSupplier()

def updateSupplier(supplier_id,name,code,is_active):
    qryRes = supplier.query.filter_by(supplier_id = supplier_id).all()
    r = qryRes[0]
    r.name = name
    r.code = code
    r.is_active = is_active
    safeFlush()
    safeCommit()
    return getAllSupplier()

def getSupplier(supplier_id):
    qryRes = supplier.query.filter_by(supplier_id = supplier_id).all()

    if qryRes:
        return  [i.serialize for i in qryRes]
    else:
        pass

def deleteSupplier(supplier_id):
    qryRes = supplier.query.filter_by(supplier_id = supplier_id).all()
    r = qryRes[0]

    db.session.delete(r)
    safeFlush()
    safeCommit()
    return getAllSupplier()
