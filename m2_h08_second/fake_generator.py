from models import Contact
from faker import Faker

def generate_fake_contact():
    fake_data = Faker()    
    
    contact = Contact()
    contact.fullname = fake_data.name()
    contact.email = fake_data.email()
    contact.phone = fake_data.phone_number()
    contact.message_type = fake_data.random.randint(0,1)
    return contact