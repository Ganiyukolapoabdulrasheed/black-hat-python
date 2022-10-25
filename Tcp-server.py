import socket
import threading


def targetport():
    try:
        target_port = int(input("target port"))
        return target_port
    except ValueError as error:
        print(f"You made a/an {error}, No strings are allowed ")
        return targetport()

def main(IP,PORT):
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f"listening at {IP}:{PORT}")

    while True:
        client, address = server.accept()
        client_handler = threading.Thread(target=clienthandler, args=(client,))
        client_handler.start()

def clienthandler(client):
    with client as sock:
        request = sock.recv(1026)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b"ACK")

if __name__ == '__main__':
    IP = input("IP Address: ")
    PORT = targetport()
    main(IP,PORT)

        

