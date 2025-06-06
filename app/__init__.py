from flask import Flask
from flask_cors import CORS

from app.routes.homelone_adviser import homelone_advise


def create_app():
    app = Flask(__name__)
    CORS(app)

    from app.routes.investment import investment_bp
    app.register_blueprint(investment_bp)
    app.register_blueprint(homelone_advise)

    return app
