from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, RadioField
from wtforms.validators import Required, DataRequired


class PitchForm(FlaskForm):
    pitch = TextAreaField('Pitch review', validators=[Required()])
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    pitch = TextAreaField(("What's on your mind ?"),
                          validators=[DataRequired()])
    category = SelectField('Category', choices=[(
        'Pickup Lines', 'Pickup Lines'), ('About You', 'About You'), ('Interviews', 'Interviews')])

    submit = SubmitField(('post'))


class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    vote = RadioField('default field arguments', choices=[
                      ('1', 'UpVote'), ('1', 'DownVote')])
    submit = SubmitField('SUBMIT')
class UpvoteForm(FlaskForm):
    '''
    Class to create a wtf form for upvoting a pitch
    '''
    submit = SubmitField('Upvote')
   
