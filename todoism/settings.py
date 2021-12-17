import os

class BaseConfig:
    TODOISM_LOCALES = ['en_US', 'zh_Hans_CN']
    
    BABEL_DEFAULT_LOCALE = TODOISM_LOCALES[0]

    SECRET_KEY = os.getenv('SECRET_KEY', 't7LgcyCovcnCtIct5iClc7eVgh1v5ucyho/CNIjLmsY=')

    SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@%s:%s/%s' % (
        os.getenv('PG_USER', 'zhengyaqi'),
        os.getenv('PG_PASSWORD', '123456'),
        os.getenv('PG_HOST', '127.0.0.1'),
        os.getenv('PG_PORT', '5433'),
        os.getenv('PG_DATABASE', 'todoism')
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    pass

class ProductionConfig(BaseConfig):
    pass

class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}