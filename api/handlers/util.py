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
