import socket

HOST = "127.0.0.1"
PORT = 5050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -------------------------------
# 1. Timeout saat connect (3 detik)
# -------------------------------
client.settimeout(3)

try:
    client.connect((HOST, PORT))
    print("Terhubung ke server.")
except socket.timeout:
    print("Koneksi timeout! (saat connect)")
    exit()
except Exception as e:
    print("Error:", e)
    exit()

# -------------------------------
# 2. Timeout saat membaca data (2 detik)
# -------------------------------
client.settimeout(2)

try:
    data = client.recv(1024)
    print("Dari server:", data.decode())
except socket.timeout:
    print("Koneksi timeout! Silahkan menunggu 2-3 detik untuk login ")
except Exception as e:
    print("Error:", e)

client.close()
