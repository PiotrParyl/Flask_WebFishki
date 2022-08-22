from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth',__name__)


@auth.route('/login', methods=['GET','POST'])
def login():

    return render_template('login.html')

@auth.route('/signin', methods=['GET','POST'])
def signin():

    return render_template('signin.html')