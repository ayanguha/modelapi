from flask import request,render_template,make_response,jsonify,redirect,url_for
from flask_restplus import  Resource, reqparse

from ..handlers.handlers import *
from ..handlers.edicategory import *
from ..handlers.edifile import *
from ..handlers.accrual_task_status_details import *
from ..handlers.supplier import *
from ..handlers.glaccount import *
from ..handlers.files import *


############################################################################################
def getUIConfig():
    uiconfig = {}
    uiconfig['backgrouound_color'] = '#5cb85c'
    uiconfig['localenv'] = 'dev'

    return uiconfig

############################################################################################
class UIHandler(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(
                render_template('index.html',  uiconfig=getUIConfig()), 200,headers)

############################################################################################

class SampleUIHandler(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}
        afs = getAllAccount()
        print(afs)
        return make_response(
                render_template('sample.html',uiconfig=getUIConfig(),
                             lst=afs ), 200,headers)
############################################################################################

############################################################################################

class AlertsUIHandler(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}
        aaa = getAllAlerts()
        return make_response(
                render_template('file_history.html',uiconfig=getUIConfig(),
                             lst=aaa ), 200,headers)
############################################################################################

############################################################################################

class FileHistoryUIHandler(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}
        aaa = getAllFiles()
        return make_response(
                render_template('file_history.html',uiconfig=getUIConfig(),
                             lst=aaa ), 200,headers)
############################################################################################

############################################################################################

class SingleFileUIHandler(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}
        afs = getSingleFile(request.args.get('file_name'))
        return make_response(
                render_template('single_file.html',uiconfig=getUIConfig(),
                             lst=afs ), 200,headers)
############################################################################################

############################################################################################

class EdicategoryUIHandler(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}
        afs = getAllEdiCategory()
        print(afs)
        return make_response(
                render_template('edi_category.html',uiconfig=getUIConfig(),
                             lst=afs ), 200,headers)
############################################################################################
############################################################################################

class EdifileUIHandler(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}
        afs = getAlledifile()
        print(afs)
        return make_response(
                render_template('edi_file.html',uiconfig=getUIConfig(),
                             lst=afs ), 200,headers)
############################################################################################

############################################################################################

class SupplierUIHandler(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}
        afs = getAllSupplier()
        print(afs)
        return make_response(
                render_template('supplier.html',uiconfig=getUIConfig(),
                             lst=afs ), 200,headers)
############################################################################################

############################################################################################

class GlAccountUIHandler(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}
        afs = getAllGlaccount()
        print(afs)
        return make_response(
                render_template('glaccount.html',uiconfig=getUIConfig(),
                             lst=afs ), 200,headers)
############################################################################################

############################################################################################

class AccrualTaskStatusDetailsUIHandler(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}
        afs = getAllAccrualTaskStatusDetails()
        print(afs)
        return make_response(
                render_template('accrual_task_status_details.html',uiconfig=getUIConfig(),
                             lst=afs ), 200,headers)
############################################################################################
