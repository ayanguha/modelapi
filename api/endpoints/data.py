from flask import request,url_for,render_template,make_response,jsonify,redirect,url_for,flash
from flask_restplus import Resource,fields,reqparse
from ..handlers.handlers import *
from ..handlers.edicategory import *
from ..handlers.accrual_task_status_details import *
from ..handlers.edifile import *
from ..handlers.supplier import *
from ..handlers.glaccount import *
from ..handlers.files import *
from ..handlers.transactions import *
from ..handlers.auth import *
from ..define import api
import uuid

from flask_login import login_user, logout_user, login_required


ns = api.namespace('v1')

AccountRecord = api.model('Account Record ', {
    'name': fields.String(required=True),
    'parent_account_id': fields.String()
})

BasicRecord = api.model('Simple Record ', {
    'name': fields.String(required=True)
})


TransactionHeaderRecord = api.model('Transaction Header Record ', {
    'filename': fields.String(required=True),
    'version': fields.String(required=True),
    'header_text': fields.String(required=True),
    'document_type': fields.String(required=True),
    'calc_tax': fields.String(required=False),
    'posting_date': fields.String(required=True),
    'document_date': fields.String(required=True),
    'document_reference': fields.String(required=True),
    'currency': fields.String(required=True),
    'vendor_code': fields.String(required=True),
    'total_amount': fields.String(required=True)
})

TransactionDetailsRecord = api.model('Transaction Details Record ', {
    'filename': fields.String(required=True),
    'version': fields.String(required=True),
    'line_number': fields.String(required=True),
    'posting_key': fields.String(required=True),
    'gl_account': fields.String(required=True),
    'line_amount': fields.String(required=True),
    'costcenter': fields.String(required=True),
    'line_text': fields.String(required=True),
    'emplus_ref': fields.String(required=False)
})

TransactionsRecord =  api.model('Transactions ', {
         'headers': fields.Nested(TransactionHeaderRecord),
         'details': fields.List(fields.Nested(TransactionDetailsRecord))
})

def BasicResponse(lst):
    response = BaseResponse()
    for a in lst:
        response['data'].append(a)
    return response

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

###########################################################
@ns.route('/ingest/transactions')
class TransactionsRecordRequest(Resource):
    @api.expect(TransactionsRecord)
    def post(self):

        print(request.json)
        resp = addTransactionHeader(request.json['headers'])
        resp = addTransactionDetailMany(request.json['details'])
        return BasicResponse(resp),201

###########################################################
@ns.route('/auth/login')
class LoginRequest(Resource):
    def post(self):
        next = request.args.get('next')
        user = login_user_backend(request.form['InputEmail'],request.form['InputPassword'])
        if not user:
            return redirect(url_for('api.login_ui_handler'))
        login_user(user)
        flash('Logged in successfully.')
        return redirect(next or url_for('api.ui_handler'))
    

@ns.route('/logout')
class LogoutRequest(Resource):
    @login_required
    def post(self):
        logout_user()
        return redirect(url_for('api.login_ui_handler'))


###########################################################
@ns.route('/dbm/edi_category')
class EDICategoryRequest(Resource):
    @api.expect(BasicRecord)
    def post(self):
        response = addEdiCategory(request.json['name'])
        return BasicResponse(response),201

    def get(self):
        response = getAllEdiCategory()
        return BasicResponse(response), 200

@ns.route('/dbm/edi_category/<string:edi_category_id>')
class SingleEDICategoryRequest(Resource):
    def put(self, edi_category_id):
        response = updateEdiCategory(edi_category_id, request.json['name'])
        return BasicResponse(response),201

    def get(self, edi_category_id):
        response = getEdiCategory(edi_category_id)
        return BasicResponse(response), 200

    def delete(self, edi_category_id):
        response = deleteEdiCategory(edi_category_id)
        return BasicResponse(response), 200

###########################################################
@ns.route('/dbm/edi_file')
class EDIFileRequest(Resource):
    @api.expect(BasicRecord)
    def post(self):
        response = addEdifile(request.json['name'])
        return BasicResponse(response),201

    def get(self):
        response = getAllEdiFile()
        return BasicResponse(response), 200

@ns.route('/dbm/edi_file/<string:edifile_id>')
class SingleEDIFileRequest(Resource):
    def put(self, edifile_id):
        response = updateEdiFile(edifile_id, request.json['name'])
        return BasicResponse(response),201

    def get(self, edifile_id):
        response = getEdiFile(edifile_id)
        return BasicResponse(response), 200

    def delete(self, edifile_id):
        response = deleteEdiFile(edifile_id)
        return BasicResponse(response), 200



###########################################################
@ns.route('/dbm/accrual_task_status_details')
class AccrualTaskStatusDetailsRequest(Resource):
    @api.expect(BasicRecord)
    def post(self):

        response = addAccrualTaskStatusDetails(request.json['status'], request.json['include'])
        return BasicResponse(response),201

    def get(self):
        response = getAllAccrualTaskStatusDetails()
        return BasicResponse(response), 200

@ns.route('/dbm/accrual_task_status_details/<string:accrual_task_status_details_id>')
class SingleAccrualTaskStatusDetailsRequest(Resource):
    def put(self, accrual_task_status_details_id):

        response = updateAccrualTaskStatusDetails(accrual_task_status_details_id, request.json['status'], request.json['include'])
        return BasicResponse(response),201

    def get(self, accrual_task_status_details_id):
        response = getAccrualTaskStatusDetails(accrual_task_status_details_id)
        print(response)
        return BasicResponse(response), 200

    def delete(self, accrual_task_status_details_id):
        response = deleteAccrualTaskStatusDetails(accrual_task_status_details_id)
        return BasicResponse(response), 200

###########################################################
@ns.route('/dbm/supplier')
class SupplierRequest(Resource):
    @api.expect(BasicRecord)
    def post(self):

        response = addSupplier(request.json['name'], request.json['code'], request.json['is_active'])
        return BasicResponse(response),201

    def get(self):
        response = getAllSupplier()
        return BasicResponse(response), 200

@ns.route('/dbm/supplier/<string:supplier_id>')
class SingleSupplierRequest(Resource):
    def put(self, supplier_id):

        response = updateSupplier(supplier_id, request.json['name'], request.json['code'], request.json['is_active'])
        return BasicResponse(response),201

    def get(self, supplier_id):
        response = getSupplier(supplier_id)
        print(response)
        return BasicResponse(response), 200

    def delete(self, supplier_id):
        response = deleteSupplier(supplier_id)
        return BasicResponse(response), 200

###########################################################
@ns.route('/dbm/glaccount')
class GlAccountRequest(Resource):
    @api.expect(BasicRecord)
    def post(self):

        response = addGlaccount(request.json['code'], request.json['description'], request.json['financial_type'], request.json['is_active'])
        return BasicResponse(response),201

    def get(self):
        response = getAllGlaccount()
        return BasicResponse(response), 200

@ns.route('/dbm/glaccount/<string:glaccount_id>')
class SingleGlAccountRequest(Resource):
    def put(self, glaccount_id):


        response = updateGlaccount(glaccount_id, request.json['code'], request.json['description'], request.json['financial_type'], request.json['is_active'])
        return BasicResponse(response),201

    def get(self, glaccount_id):
        response = getGlaccount(glaccount_id)
        return BasicResponse(response), 200

    def delete(self, glaccount_id):
        response = deleteGlaccount(glaccount_id)
        return BasicResponse(response), 200
