import os


class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    ### OLD LOCAL DATABASE 
    ### SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    ### NEW POSTGRESQL DATABASE
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@10.1.30.198:5432/webapp'
    MAIL_SERVER = 'smtp.outlook.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'balaolab3@outlook.com'
    MAIL_PASSWORD = ''