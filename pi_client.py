import socket
import threading

# def start_client():
#     SERVER_HOST = '192.168.43.69'  # or the server's IP address
#     SERVER_PORT = 12345

#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
#     try:
#         client_socket.connect((SERVER_HOST, SERVER_PORT))
#         print("Connected to server.")
        
#         while True:
#             message = "Hello from the client!"
#             client_socket.sendall(message.encode())
#             print("Message sent to server.")
            
#             response = client_socket.recv(1024)
#             print(f"Received from server: {response.decode()}")
#     except Exception as e:
#         print(f"Error: {e}")
#     finally:
#         print("!!!! closing connection !!!")
#         client_socket.close()

# if __name__ == '__main__':
#     start_client()

class SocketClient:
    
    def __init__(self):
        
        self.CLIENT_HOST = "192.168.43.69"
        self.CLIENT_PORT = 12345
        
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.connected = False
        
        connect_to_server_thread = threading.Thread(target = self.connect_to_server)
        connect_to_server_thread.daemeon = True
        connect_to_server_thread.start()
        
    
    def connect_to_server(self):
        """
        Function to establish connection with client.
        """
        while not self.connected:
            try:
                self.client_socket.connect((self.CLIENT_HOST,self.CLIENT_PORT))
                self.connected = True
            except ConnectionRefusedError:
                print(f"***** Retrying connection to server ********")
            
            
        print("---- Connected to server -----")
        
    def __del__(self):
        self.client_socket.close()
        
        
if __name__ == "__main__":
    
    client = SocketClient()
    
    while True:
        print(f"####### connect flag : {client.connected} ##############")