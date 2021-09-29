from ..database import db
from ..database.orms import *
from sqlalchemy.orm.exc import NoResultFound
from flask_restplus import reqparse
from datetime import datetime
from flask import request,url_for,render_template,make_response,jsonify,redirect,url_for
import random, json,os
from .util import *


def getAllTransactionHeaders():
    qryRes = transactionheader.query.all()
    return [i.serialize for i in qryRes]

def addTransactionHeader(payload):

    r = transactionheader(payload)

    db.session.add(r)
    safeFlush()
    safeCommit()
    return getAllTransactionHeaders()

def getAllTransactionDetails():
    qryRes = transactiondetail.query.all()
    return [i.serialize for i in qryRes]

def addTransactionDetailMany(payload):
    for p in payload:
        r = transactiondetail(p)
        db.session.add(r)
    safeFlush()
    safeCommit()
    return getAllTransactionHeaders()
