import socket
import threading

HOST = "0.0.0.0"
PORT = 5050

clients = []     # Menyimpan list semua client
lock = threading.Lock()

def broadcast(message, sender_socket=None):
    """Kirim pesan ke semua client kecuali pengirim."""
    with lock:
        for client in clients:
            if client != sender_socket:
                try:
                    client.send(message)
                except:
                    client.close()
                    clients.remove(client)

def handle_client(client_socket, addr):
    print(f"[CONNECTED] {addr} terhubung")
    client_socket.send(b"Selamat datang di Chat Server!\n")

    while True:
        try:
            msg = client_socket.recv(1024)
            if not msg:
                break

            print(f"[{addr}] {msg.decode().strip()}")

            # Broadcast ke client lain
            broadcast(msg, sender_socket=client_socket)

        except:
            break

    print(f"[DISCONNECTED] {addr} keluar")
    with lock:
        clients.remove(client_socket)
    client_socket.close()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    print(f"[SERVER READY] Listening on port {PORT} ...")

    while True:
        client_socket, addr = server.accept()
        with lock:
            clients.append(client_socket)

        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()


if __name__ == "__main__":
    main()
