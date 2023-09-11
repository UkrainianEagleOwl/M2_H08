

from connect_mongoengine import do_connect_to_db
from fake_generator import generate_fake_contact
import pika


# Create a connection to RabbitMQ
credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

# Declare a queue to send messages
queue_name_sms = 'contacts_sms_queue'
queue_name_email = 'contacts_emails_queue'
channel.queue_declare(queue=queue_name_sms)
channel.queue_declare(queue=queue_name_email)

def main():
    do_connect_to_db("M2_H08_2")
    for i in range(10):
        contact = generate_fake_contact()
        contact.save()
        
        # Queue a RabbitMQ message containing the ObjectID of the generated contact
        message = str(contact.id)
        if contact.message_type == 0:
            channel.basic_publish(exchange='', routing_key=queue_name_email, body=message)
        else:
            channel.basic_publish(exchange='', routing_key=queue_name_sms, body=message)
        print(f"Queued contact with ID: {contact.id}")
        
    # Close the RabbitMQ connection
    connection.close()


if __name__ == "__main__":
    main()

