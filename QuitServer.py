import pika
import sys


def quit_callback(ch, method, props, body):
    """Callback function to handle quit messages."""
    message = body.decode()
    if message == 'Y':
        print("Exiting program...")
        ch.basic_ack(delivery_tag=method.delivery_tag)
        response = "Server is shutting down"
        ch.basic_publish(
            exchange='',
            routing_key=props.reply_to,
            properties=pika.BasicProperties(correlation_id=props.correlation_id),
            body=response
        )
        ch.stop_consuming()
        ch.connection.close()
        sys.exit()
    elif message == 'N':
        print("Continuing operation...")
        response = "Server is continuing"
        ch.basic_publish(
            exchange='',
            routing_key=props.reply_to,
            properties=pika.BasicProperties(correlation_id=props.correlation_id),
            body=response
        )
        ch.basic_ack(delivery_tag=method.delivery_tag)
    else:
        print("Invalid input received, ignoring...")
        response = "Invalid input"
        ch.basic_publish(
            exchange='',
            routing_key=props.reply_to,
            properties=pika.BasicProperties(correlation_id=props.correlation_id),
            body=response
        )
        ch.basic_ack(delivery_tag=method.delivery_tag)

def start_quit_server():
    """Function to start the QuitServer."""
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='QuitQueue')

    channel.basic_consume(queue='QuitQueue', on_message_callback=quit_callback)

    print('Waiting for quit messages...')
    channel.start_consuming()

if __name__ == "__main__":
    start_quit_server()