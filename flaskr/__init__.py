from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

app=Flask(__name__)
app.config['CLIENT_IMAGES']='c:/Users/DELL/official/Nautilus3/flaskr/static/client/file'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Nautilus5he!@localhost:5432/save'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate=Migrate(app,db)

from flaskr import app