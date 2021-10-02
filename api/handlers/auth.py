from ..database import db
from ..database.orms import *
from sqlalchemy.orm.exc import NoResultFound
from flask_restplus import reqparse
from datetime import datetime
from flask import request,url_for,render_template,make_response,jsonify,redirect,url_for
import random, json,os
from .util import *


def login_user_backend(email, password_clear):
    user = User.query.filter_by(email = email).first()
    if not user:
        return None
    return user
