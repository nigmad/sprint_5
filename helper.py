from faker import Faker
faker = Faker()

def generate_registration_data():
    name = faker.name()
    email = faker.email()
    password = faker.password(length=6)
    return name, email, password
