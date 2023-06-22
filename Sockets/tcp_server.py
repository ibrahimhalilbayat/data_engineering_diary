import socket
import json

def main():
    TYPE_OF_NETWORK_ADRESS = socket.AF_INET
    THE_PROTOCOL = socket.SOCK_STREAM # TCP

    THE_LEVEL = socket.SOL_SOCKET
    THE_OPTION = socket.SO_REUSEADDR
    THE_VALUE = 1
    
    with socket.socket(TYPE_OF_NETWORK_ADRESS, THE_PROTOCOL) as the_socket:

        the_socket.setsockopt(THE_LEVEL, THE_OPTION, THE_VALUE)
        the_socket.bind(("localhost", 8000))
        the_socket.listen()

        the_socket.settimeout(1)

        while True:
            try: 
                CLIENT_SOCKET, ADRESS = the_socket.accept()

            except socket.timeout:
                continue

            print(f"Connected from: {ADRESS[0]}")

            with CLIENT_SOCKET:
                the_messages = []

                while True:
                    try:
                        the_data = CLIENT_SOCKET.recv(4096)
                    
                    except socket.timeout:
                        continue

                    if not the_data:
                        break

                    the_messages.append(the_data)

            # Decode list-of-byte-strings to UTF8 and parse JSON data
            message_bytes = b''.join(the_messages)
            message_str = message_bytes.decode("utf-8")

            try:
                message_dict = json.loads(message_str)
            except json.JSONDecodeError:
                continue
            print(f"The message: {message_dict['message']}")


if __name__ == "__main__":
    main()
