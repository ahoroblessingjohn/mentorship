from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY']= 'f0fc14b08995b4cbd607ed82031ed0839214f47d6750c73ebd4d0b0422093a8ef3f724'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)



from main import routes