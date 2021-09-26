from ..database import db
from ..database.orms import *
from sqlalchemy.orm.exc import NoResultFound
from flask_restplus import reqparse
from datetime import datetime
from flask import request,url_for,render_template,make_response,jsonify,redirect,url_for
import random, json,os
from .util import *


def getAllEdiCategory():
    qryRes = edicategory\
                  .query\
                  .all()
    return [i.serialize for i in qryRes]

def addEdiCategory(name):
    payload = {}
    payload['name'] = name
    r = edicategory(payload)

    db.session.add(r)
    safeFlush()
    safeCommit()
    return getAllEdiCategory()

def updateEdiCategory(edi_category_id,name):
    qryRes = edicategory.query.filter_by(edi_category_id = edi_category_id).all()
    r = qryRes[0]
    r.name = name
    safeFlush()
    safeCommit()
    return getAllEdiCategory()

def getEdiCategory(edi_category_id):
    qryRes = edicategory.query.filter_by(edi_category_id = edi_category_id).all()

    if qryRes:
        return  [i.serialize for i in qryRes]
    else:
        pass

def deleteEdiCategory(edi_category_id):
    qryRes = edicategory.query.filter_by(edi_category_id = edi_category_id).all()
    r = qryRes[0]

    db.session.delete(r)
    safeFlush()
    safeCommit()
    return getAllEdiCategory()
