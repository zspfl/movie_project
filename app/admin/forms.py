#encoding:utf8
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,ValidationError
from app.models import Admin
class LoginForm(FlaskForm):
    '''admin login form'''
    account = StringField(
        label='account',
        validators=[
            DataRequired('account is required')
        ],
        description='account',
        render_kw={
            "class":"form-control",
            "placeholder":"please input account",
            'required':"required"
        }
    )
    pwd = PasswordField(
        label='password',
        validators=[
            DataRequired('pleae input password')
        ],
        description='password',
        render_kw={
            "class":"form-control",
            "placeholder":"please input password",
            "required":"required"
        }
    )
    submit = SubmitField(
        "Login",
        render_kw={
            "class":"btn btn-primary btn-block btn-flat"
        }
    )

    def validate_account(self,field):
        account = field.data
        admin = Admin.query.filter_by(name=account).count()
        if admin ==0:
            raise ValidationError("account not exist")

class TagForm(FlaskForm):
    name = StringField(
        label="name",
        validators=[
            DataRequired("please input the tag")
        ],
        description="name",
        render_kw={
            "class":"form-control",
            "id":"input_name",
            "placeholder":"please input the tag name"
        }
    )
    submit = SubmitField(
        "Add",
        render_kw={
            "class": "btn btn-primary"
        }
    )