import socket

def main():
    host = input("Adresse du serveur [127.0.0.1]: ").strip() or "127.0.0.1"
    port = int(input("Port [5000]: ").strip() or "5000")
    s = socket.socket()
    try:
        print(f"Connexion à {host}:{port}...")
        s.connect((host, port))
        print("Connecté. Tapez votre message.")
    except Exception as e:
        print("Échec de la connexion:", e)
        return

    try:
        while True:
            msg = input("Toi : ")
            if not msg:
                continue
            s.send(msg.encode())
            data = s.recv(1024)
            if not data:
                print("Connexion fermée par le serveur.")
                break
            print("Lui :", data.decode())
    except KeyboardInterrupt:
        print("\nArrêt demandé.")
    finally:
        s.close()

if __name__ == "__main__":
    main()
