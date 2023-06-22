import socket
import json


def main():

    TYPE_OF_NETWORK_ADRESS = socket.AF_INET
    THE_PROTOCOL = socket.SOCK_DGRAM # TCP

    while True:

        input_message_fom_user = input("Please write your messsage here: ")

        with socket.socket(TYPE_OF_NETWORK_ADRESS, THE_PROTOCOL) as the_socket:

            the_socket.connect(("localhost", 8002))

            # send a message
            message = json.dumps({"message": input_message_fom_user})
            the_socket.sendall(message.encode('utf-8'))


if __name__ == "__main__":
    main()
