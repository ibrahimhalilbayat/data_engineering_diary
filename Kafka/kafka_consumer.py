from kafka import KafkaConsumer

# Let's create the configuration
conf = {
    "bootstrap_servers": "localhost:9092",
    "group_id": "bayat_group"
}

the_consumer = KafkaConsumer(**conf)

the_topics = ["destroying-ring"]

try:
    the_consumer.subscribe(topics=the_topics)

    while True:
        messages = the_consumer.poll(timeout_ms=1000)  # Adjust the timeout as needed

        for tp, messages in messages.items():
            for message in messages:

                value = message.value.decode("utf-8")
                print(f"Received message: {value}")

except Exception as e:
    print(f"An exception occurred: {e}")

finally:
    the_consumer.close()
