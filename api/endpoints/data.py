from flask import request,url_for,render_template,make_response,jsonify,redirect,url_for
from flask_restplus import Resource,fields,reqparse
from ..handlers.handlers import *
from ..define import api
import uuid

ns = api.namespace('v1')

AccountRecord = api.model('Account Record ', {
    'name': fields.String(required=True),
    'parent_account_id': fields.String()
})

def parseInputDatetime(s):
    return  datetime.strptime(s,'%Y-%m-%dT%H:%M:%S.%fZ')

CommonParser = reqparse.RequestParser()
CommonParser.add_argument('fields',  help="List of fields. Format: Comma separated list of fields",type=str)
CommonParser.add_argument('start_datetime',  help="Start Generated On Time. Format:'%Y-%m-%dT%H:%M:%S.%fZ",type=parseInputDatetime)
CommonParser.add_argument('end_datetime',  help="End Generated On Time. Format:'%Y-%m-%dT%H:%M:%S.%fZ",type=parseInputDatetime)

def parse_params(req):
    a = {}
    for r in req.args:
        a[r] = req.args[r]



def BaseResponse():
    baseresponse = {
                     "data": [],
                     "meta": {"limit": 20,"next": None,"offset": 0,"previous": None}
                   }
    return baseresponse

def AccountResponse(list_account):
    account_response = BaseResponse()
    for a in list_account:
        account_response['data'].append(a)
    return account_response


@ns.route('/account')
class AccountRecordRequest(Resource):
    @api.expect(AccountRecord)
    def post(self):
        print(request.json)
        response = createAccount(request)
        return AccountResponse(response),201

    def get(self):
        args = CommonParser.parse_args(request)
        print(args)
        response = getAllAccount()
        return AccountResponse(response), 200

@ns.route('/account/<string:account_id>')
class SingleAccountRequest(Resource):

    def get(self,account_id):
        params = parse_params(request)
        response = getSingleAccount(account_id)
        return AccountResponse(response), 200

'''
@ns.route('/device')
class Device(Resource):
    @api.expect(DeviceRecordRequest)
    def post(self):
        print(request.json)
        response = {'id': createDevice(request.json)}
        return response,201

    def get(self):
        response = {'data': {}}
        return response, 200

@ns.route('/device/<string:device_id>')
class SingleDevice(Resource):
    def get(self,device_id):
        did = getSingleDevice(device_id)
        response = {'idUrl': url_for('api.v1_single_device',device_id=did, _external=True)}
        return response, 200
'''
