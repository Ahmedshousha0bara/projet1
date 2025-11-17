import socket

def main():
    host = "0.0.0.0"
    port = int(input("Port [5000]: ").strip() or "5000")
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        s.bind((host, port))
    except OSError as e:
        print("Échec du bind:", e)
        print("Vérifiez si un autre programme utilise ce port, ou choisissez un port différent.")
        return
    s.listen(1)
    print(f"Serveur en écoute sur {host}:{port} ...")
    conn, addr = s.accept()
    print("Connexion depuis", addr)
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                print("Client déconnecté.")
                break
            print("Lui :", data.decode())
            msg = input("Toi : ")
            if not msg:
                continue
            conn.send(msg.encode())
    except KeyboardInterrupt:
        print("\nArrêt serveur.")
    finally:
        conn.close()
        s.close()

if __name__ == "__main__":
    main()
