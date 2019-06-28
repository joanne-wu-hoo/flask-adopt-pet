from flask import Flask, render_template, request, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm
from secrets import PET_FINDER_API_KEY, SECRET_PET_FINDER_API_KEY
from api import get_pet_info

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route("/")
def list_all_pets():
    """ List all pets """
    # Pets from database
    pets = Pet.query.all()
    # Random pet finder pet
    pet_finder_pet = get_pet_info()
    return render_template("list_pets.html", pets=pets, pet_finder_pet=pet_finder_pet)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """ Pet add form; handle adding """

    form = AddPetForm()

    if form.validate_on_submit():
        # Grab values from form
        pet_name = form.pet_name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        # If photo_url input is blank, set to None so that database will input default URL
        if photo_url == "":
            photo_url = None

        # Add pet to database
        new_pet = Pet(name=pet_name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()

        flash(f"{pet_name} added!", "success")
        return redirect("/")

    else:
        return render_template("show_add_pet_form.html", form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def handle_editing_of_pet_info(pet_id):
    """ Handle editing of pet info """
    pet = Pet.query.get(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        # Grab inputs from from
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data

        # Edit pet in database
        pet.photo_url = photo_url
        pet.notes = notes
        pet.available = available
        db.session.commit()

        flash(f"{pet.name}'s information was succesfully edited", "success")
        return redirect("/")
    else:
        return render_template("show_pet_info_and_edit_form.html", pet=pet, form=form)

