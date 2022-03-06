from crudsql import db

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    species = db.Column(db.String(40), nullable=False)
    breed = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return f'Pet({self.name}, {self.species}, {self.breed})'