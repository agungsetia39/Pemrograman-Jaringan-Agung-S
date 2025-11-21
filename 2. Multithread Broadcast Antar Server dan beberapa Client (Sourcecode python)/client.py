import socket
import threading

HOST = "127.0.0.1"
PORT = 5050

def receive(sock):
    while True:
        try:
            msg = sock.recv(1024)
            if msg:
                print("\n" + msg.decode(), end="")
        except:
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    threading.Thread(target=receive, args=(client,), daemon=True).start()

    print("Terhubung ke server.")
    while True:
        msg = input("")
        client.send(msg.encode())

if __name__ == "__main__":
    main()
