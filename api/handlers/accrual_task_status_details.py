from ..database import db
from ..database.orms import *
from sqlalchemy.orm.exc import NoResultFound
from flask_restplus import reqparse
from datetime import datetime
from flask import request,url_for,render_template,make_response,jsonify,redirect,url_for
import random, json,os
from .util import *


def getAllAccrualTaskStatusDetails():
    createAllModels(db)
    qryRes = accrual_task_status_details.query.all()
    return [i.serialize for i in qryRes]

def addAccrualTaskStatusDetails(status, include):
    payload = {}
    payload['status'] = status
    payload['include'] = include
    r = accrual_task_status_details(payload)

    db.session.add(r)
    safeFlush()
    safeCommit()
    return getAllAccrualTaskStatusDetails()

def updateAccrualTaskStatusDetails(accrual_task_status_details_id,status, include):
    qryRes = accrual_task_status_details.query.filter_by(accrual_task_status_details_id = accrual_task_status_details_id).all()
    r = qryRes[0]
    r.status = status
    r.include = include
    safeFlush()
    safeCommit()
    return getAllAccrualTaskStatusDetails()

def getAccrualTaskStatusDetails(accrual_task_status_details_id):
    qryRes = accrual_task_status_details.query.filter_by(accrual_task_status_details_id = accrual_task_status_details_id).all()

    if qryRes:
        return  [i.serialize for i in qryRes]
    else:
        pass

def deleteAccrualTaskStatusDetails(accrual_task_status_details_id):
    qryRes = accrual_task_status_details.query.filter_by(accrual_task_status_details_id = accrual_task_status_details_id).all()
    r = qryRes[0]

    db.session.delete(r)
    safeFlush()
    safeCommit()
    return getAllAccrualTaskStatusDetails()
