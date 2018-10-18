import os 


class Config():

    SECRET_KEY = 'af2266ddaec003c6e70a5d266db213dd'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = '' # os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = '' # os.environ.get('EMAIL_PASS')