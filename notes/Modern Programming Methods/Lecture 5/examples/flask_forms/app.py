import os

from flask import Flask, request, redirect,\
    url_for, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField
from wtforms.validators import DataRequired

from game import PaperScissorsStone

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET',
                                'BadDefault')


CHOICES = ['paper', 'scissors', 'stone']
MAPPING = {val: key for key, val in enumerate(CHOICES)}

GAME = PaperScissorsStone()


class GameForm(FlaskForm):
    # paper = SubmitField('Paper')
    # scissors = SubmitField('Scissors')
    # stone = SubmitField('Stone')
    user_name = StringField(
        label = 'user_name',
        validators = [
            DataRequired(message = 'Your Name'),
        ]
    )
    animal = StringField(
        label = 'animal',
        validators =[
            DataRequired(message = 'Come on, you must have a favorite animal!'),
        ]
    )
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():

    info = []
    animal_pic = []
    gform = GameForm()

    if request.method == 'POST':
        # choice = (MAPPING.keys() & request.form.keys()).pop()

        player_name = str(request.form.get('user_name'))
        player_animal = str(request.form.get('animal'))
        info.append(player_name)
        info.append(player_animal)
        # result, my_choice = GAME.play_round(MAPPING[choice])
        print(player_name)
        print(player_animal)



    return render_template('index.html', info=info, game = GAME,
                           form=gform)
