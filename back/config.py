class Config:
    URL = "http://127.0.0.1:5000"

class ProductionConfig(Config):
    DEBUG  = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:PruebA01@localhost:5432/postgres"
    SQLALCHEMY_TRACK_MODIFICATIONS = False 

class DevelopmentConfig(Config):
    DEBUG  = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False 

config = {
    'production': ProductionConfig,
	'development': DevelopmentConfig
}