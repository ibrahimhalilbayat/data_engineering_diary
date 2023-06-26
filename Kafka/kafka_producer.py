import socket
from kafka import KafkaProducer
import time

# Let's create the configurations
conf = {
    "bootstrap_servers": "localhost:9092",
    "client_id": socket.gethostname()
}

# Create the Kafka producer based on this configuration
the_producer = KafkaProducer(**conf)

def the_message(err, msg):
    if err is not None:
        print(f"An error occurred. Error: {str(err)}. Message: {str(msg)}")
    else:
        print(f"Message has been sent: {str(msg)}")

counter = 0

while True:

    counter += 2
    str_counter = str(counter)*4
    print(f"The message is: {str_counter}")

    the_producer.send("destroying-ring", key=b"1111", value="{}".format(str_counter).encode()).add_callback(the_message)
    the_producer.flush()
    time.sleep(5)

