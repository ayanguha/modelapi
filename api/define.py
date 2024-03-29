import traceback

from flask_restplus import Api
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError


api = Api(version='1.0', title='Model API',doc='/doc/',
          description='Model Data Management API')

@api.errorhandler(IntegrityError)
def database_dups_handler(e):

    return {'message': str(e.orig.args[1])}, 500


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'

    return {'message': message}, 500


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    return {'message': 'A database result was required but none was found.'}, 404
