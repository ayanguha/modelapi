
from flask import Flask,request,Response,jsonify,Blueprint
from flask_sqlalchemy import SQLAlchemy
from api.endpoints.data import ns as dataNS
from api.define import api
from api.endpoints.ui import *

import settings
from api.handlers.handlers import db

app = Flask(__name__)

pageUIMapping = [ [UIHandler,"/"],
                  [UIHandler,"/ui"] ,
                  [UIHandler,"/ui/"],
                  [SampleUIHandler,"/ui/sample"],
                  [AlertsUIHandler, "/ui/alerts"],

                  [FileHistoryUIHandler, "/ui/file_history"],
                  [SingleFileUIHandler, "/ui/single_file"],

                  [EdicategoryUIHandler, "/ui/edicategory"],
                  [AccrualTaskStatusDetailsUIHandler, "/ui/accrual_task_status_details"],

                 ]

def configure_app(flask_app):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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


initialize_app(app)


def main():

    app.run(debug=True,host='0.0.0.0',port=5010)

if __name__ == "__main__":
    main()
