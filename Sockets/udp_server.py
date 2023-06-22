import socket
import json

def main():
    TYPE_OF_NETWORK_ADRESS = socket.AF_INET
    THE_PROTOCOL = socket.SOCK_DGRAM # UDP

    THE_LEVEL = socket.SOL_SOCKET
    THE_OPTION = socket.SO_REUSEADDR
    THE_VALUE = 1
    
    with socket.socket(TYPE_OF_NETWORK_ADRESS, THE_PROTOCOL) as the_socket:

        the_socket.setsockopt(THE_LEVEL, THE_OPTION, THE_VALUE)
        the_socket.bind(("localhost", 8002))
        the_socket.settimeout(1)

        while True:
            try:
                message_bytes = the_socket.recv(4096)
            except socket.timeout:
                continue
            message_str = message_bytes.decode("utf-8")
            message_dict = json.loads(message_str)
            print(f"The message: {message_dict['message']}")


if __name__ == "__main__":
    main()
