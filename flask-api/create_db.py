from api import app, db, UserModel
from faker import Faker
import os

faker = Faker()

def delete_existing_db():
    db_path = app.config['SQLALCHEMY_DATABASE_URI'].replace('sqlite:///', '')
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"Deleted existing database at {db_path}")

with app.app_context():
    db.create_all()

    test_users = [
        UserModel(name=faker.name(), email=faker.email()) for _ in range(10)
    ]

    db.session.bulk_save_objects(test_users)
    db.session.commit()

    print("Database created and test users added")