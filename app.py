
from flask import Flask,request,Response,jsonify,Blueprint,flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from api.endpoints.data import ns as dataNS
from api.define import api
from api.endpoints.ui import *

import settings
from api.handlers.handlers import db
from api.database.orms import *

app = Flask(__name__)

pageUIMapping = [ [UIHandler,"/"],
                  [UIHandler,"/ui"] ,
                  [UIHandler,"/ui/"],
                  [LoginUIHandler,'/ui/login'],
                  [SampleUIHandler,"/ui/sample"],
                  [AlertsUIHandler, "/ui/alerts"],

                  [FileHistoryUIHandler, "/ui/file_history"],
                  [SingleFileUIHandler, "/ui/single_file"],

                  [EdicategoryUIHandler, "/ui/edicategory"],
                  [EdifileUIHandler, "/ui/edifile"],
                  [SupplierUIHandler, "/ui/supplier"],
                  [GlAccountUIHandler, "/ui/glaccount"],
                  [AccrualTaskStatusDetailsUIHandler, "/ui/accrual_task_status_details"],

                 ]

def configure_app(flask_app):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.config['SECRET_KEY'] = "_5#y2LF4Q8z\n\xec]/"
    #flask_app.config['SESSION_TYPE'] = 'filesystem'
    flask_app.config['SESSION_PERMANENT']= False

def initialize_app(flask_app):
    configure_app(flask_app)
    blueprint = Blueprint('api', __name__)
    api.init_app(blueprint)
    api.add_namespace(dataNS)
    for pm in pageUIMapping:
        handler = pm[0]
        path = pm[1]
        api.add_resource(handler,path)

    flask_app.register_blueprint(blueprint)
    db.app = flask_app
    db.init_app(flask_app)
    login_manager = LoginManager()
    login_manager.login_view = 'api.login_ui_handler'
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))



initialize_app(app)


def main():

    app.run(debug=True,host='0.0.0.0',port=5010)

if __name__ == "__main__":
    main()
