from flask import Blueprint

release_blueprint = Blueprint(name='release_blueprint', import_name=__name__, url_prefix='/release')

root_blueprint = Blueprint(name='root_blueprint',import_name=__name__)