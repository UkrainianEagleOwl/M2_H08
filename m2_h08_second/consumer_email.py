import pika
from models import Contact
from connect_mongoengine import do_connect_to_db

# Create a connection to RabbitMQ
credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

# Declare a queue to send messages
queue_name_email = 'contacts_emails_queue'
channel.queue_declare(queue=queue_name_email)

def send_email(contact_id):
    # Simulate sending an email (replace this with your email sending logic)
    print(f"Simulating sending an email to contact with ID: {contact_id}")
    
def callback(ch, method, properties, body):
    # Convert the message body back to ObjectId
    contact_id = body.decode('utf-8')
    
    # Update the logical field for the contact
    contact = Contact.objects(id=contact_id).first()
    if contact:
        contact.subscribed = True
        contact.save()
        send_email(contact_id)
        print(f"Updated contact with ID: {contact_id}")

# Set up the consumer
channel.basic_consume(queue=queue_name_email, on_message_callback=callback, auto_ack=True)

def main():
    do_connect_to_db("M2_H08_2")
    
    print("Consumer is waiting for messages. To exit, press Ctrl+C")
    
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print("Consumer terminated.")

if __name__ == "__main__":
    main()