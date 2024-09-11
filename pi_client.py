import socket

def start_client():
    SERVER_HOST = '192.168.43.69'  # or the server's IP address
    SERVER_PORT = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        print("Connected to server.")
        
        while True:
            message = "Hello from the client!"
            client_socket.sendall(message.encode())
            print("Message sent to server.")
            
            response = client_socket.recv(1024)
            print(f"Received from server: {response.decode()}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("!!!! closing connection !!!")
        client_socket.close()

if __name__ == '__main__':
    start_client()
