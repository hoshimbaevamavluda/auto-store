from faker import Faker

fake = Faker()

def generate_user():
    return {
        "name": fake.name(),
        "last_name": fake.last_name(),
        "email": fake.unique.email(),
        "address": fake.address(),
        "city": fake.city(),
        "login_name": fake.user_name(),
        "password": fake.password(),
    }