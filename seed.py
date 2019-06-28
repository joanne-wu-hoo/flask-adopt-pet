from models import Pet, db
from app import app

# Create all tables
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add pets
Woofly = Pet(name="Woofly", species="Dog", age="2", available=True)
Porchetta = Pet(name="Porchetta", species="Porcupine", age="10", available=True)
Snargle = Pet(name="Snargle", species="Cat", age="5", available=True)

db.session.add(Woofly)
db.session.add(Porchetta)
db.session.add(Snargle)

db.session.commit()
