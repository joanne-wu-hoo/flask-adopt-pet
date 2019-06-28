""" Forms for our demo Flask app. """

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf

# TO-DO
# - Case insensitive species validation OR force inputs to be Title case?
# - Don't hard code values in error messages

# List of allowed species
SPECIES_VOCAB = ["Cat", "Dog", "Porcupine"]


class AddPetForm(FlaskForm):
    """ Form for adding pet """

    pet_name = StringField(
        "Pet name",
        validators=[InputRequired()])
    species = SelectField(
        "Species",
        choices=[(species , species) for species in SPECIES_VOCAB],
        validators=[
            InputRequired(),
            AnyOf(SPECIES_VOCAB, message="Species must be either " +  ', '.join(str(species) for species in SPECIES_VOCAB))])
    photo_url = StringField("Photo URL",
        validators=[
            URL(), 
            Optional()])
    age = FloatField("Age",
        validators=[
            InputRequired(), 
            NumberRange(min=0, max=30, message="Age must be between 0 and 30")])
    notes = StringField("Notes",
        validators=[Optional()])


class EditPetForm(FlaskForm):
    """ Form for editing a pet """

    photo_url = StringField("Photo URL",
        validators=[
            URL(), 
            Optional()])
    notes = StringField("Notes",
        validators=[Optional()])
    available = BooleanField("Availability")


