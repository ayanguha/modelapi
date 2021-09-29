from ..database import db
from ..database.orms import *
from sqlalchemy.orm.exc import NoResultFound
from flask_restplus import reqparse
from datetime import datetime
from flask import request,url_for,render_template,make_response,jsonify,redirect,url_for
import random, json,os
from .util import *


def getAlledifile():
    qryRes = edifile.query.all()
    return [i.serialize for i in qryRes]

def addEdifile(name):
    payload = {}
    payload['name'] = name
    r = edifile(payload)

    db.session.add(r)
    safeFlush()
    safeCommit()
    return getAlledifile()

def updateEdiFile(edifile_id,name):
    qryRes = edifile.query.filter_by(edifile_id = edifile_id).all()
    r = qryRes[0]
    r.name = name
    safeFlush()
    safeCommit()
    return getAlledifile()

def getEdiFile(edifile_id):
    qryRes = edifile.query.filter_by(edifile_id = edifile_id).all()

    if qryRes:
        return  [i.serialize for i in qryRes]
    else:
        pass

def deleteEdiFile(edifile_id):
    qryRes = edifile.query.filter_by(edifile_id = edifile_id).all()
    r = qryRes[0]

    db.session.delete(r)
    safeFlush()
    safeCommit()
    return getAlledifile()
