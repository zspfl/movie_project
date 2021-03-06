#encoding:utf8
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect
import pymysql

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost:3306/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['SECRET_KEY'] = 'qwfaewafzvghtdhjtfykjfthytfjytfjy'
app.debug = True

db = SQLAlchemy(app)


from app.home import home as home_blueprint
from app.admin import  admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint,url_prefix="/admin")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"),404;