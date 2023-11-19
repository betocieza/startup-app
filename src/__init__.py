from flask import Flask




# Routes
from .routes import AuthRoutes, UserRoutes,FactorRoutes, IndexRoutes, StartupRoutes, PredictionRoutes
app = Flask(__name__)


def init_app(config):
    # Configuration
    app.config.from_object(config)
  
    # Blueprints
    app.register_blueprint(IndexRoutes.main, url_prefix='/')
    app.register_blueprint(AuthRoutes.main, url_prefix='/auth') 
    app.register_blueprint(UserRoutes.main, url_prefix='/users') 
    app.register_blueprint(FactorRoutes.main, url_prefix='/factors') 
    app.register_blueprint(StartupRoutes.main, url_prefix='/startups') 
    app.register_blueprint(PredictionRoutes.main, url_prefix='/predictions') 

    return app