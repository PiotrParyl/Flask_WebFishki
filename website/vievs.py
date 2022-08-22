from flask import Blueprint, render_template
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user


vievs = Blueprint('views',__name__)

@vievs.route('/play', methods=['GET', 'POST'])
def play():
    return render_template('play.html')


@vievs.route('/make', methods=['GET', 'POST'])
def make():
    return render_template('make.html')