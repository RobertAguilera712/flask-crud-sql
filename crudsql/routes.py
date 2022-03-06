from flask import render_template, url_for, flash, redirect, request
from crudsql.forms import PetForm
from crudsql.models import Pet
from crudsql import app, db


@app.route('/', methods=['GET', 'POST'])
def home():
    form = PetForm()
    pets = Pet.query.all()
    action = url_for('home')
    if request.method == 'POST':
        if form.validate_on_submit():
            name = form.name.data
            species = form.species.data
            breed = form.breed.data
            pet = Pet(name=name, species=species, breed=breed)
            db.session.add(pet)
            db.session.commit()
            flash('The pet has been saved', 'success')
            return redirect(url_for('home'))
    return render_template('index.html', form=form, pets=pets, action=action)


@app.route('/modify/<string:id>', methods=['GET', 'POST'])
def modify(id):
    form = PetForm()
    action = url_for('modify', id=id)
    pets = Pet.query.all()
    pet = Pet.query.get(id)
    if request.method == 'POST':
        if form.validate_on_submit():
            pet.name = form.name.data
            pet.species = form.species.data
            pet.breed = form.breed.data
            db.session.commit()
            flash('The pet has been modified', 'warning')
            return redirect(url_for('home'))
    form.name.data = pet.name
    form.species.data = pet.species
    form.breed.data = pet.breed
    return render_template('index.html', form=form, pets=pets, action=action)
       
       
@app.route('/delete', methods=['POST'])
def delete():
    id = request.form.get('id')
    pet = Pet.query.get(id)
    db.session.delete(pet)
    db.session.commit()
    flash('The pet has been deleted', 'danger')
    return redirect(url_for('home'))
