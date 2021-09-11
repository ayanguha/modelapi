from flask import request,render_template,make_response,jsonify,redirect,url_for
from flask_restplus import  Resource, reqparse

from ..handlers.handlers import *


############################################################################################
def getUIConfig():
    uiconfig = {}
    uiconfig['backgrouound_color'] = '#5cd65c'
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
