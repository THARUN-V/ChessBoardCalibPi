# server.py
import socket
import threading
import time

# def start_server():
#     HOST = '0.0.0.0'
#     PORT = 12345

#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind((HOST, PORT))
#     server_socket.listen()
#     print(f"Server listening on {HOST}:{PORT}")

#     conn, addr = server_socket.accept()
#     print(f"Connected by {addr}")

#     try:
#         while True:
#             data = conn.recv(1024)
#             if not data:
#                 print("No data received. Closing connection.")
#                 break
#             print(f"Received from client: {data.decode()}")
            
#             message = "Message received!"
#             conn.sendall(message.encode())
#     except Exception as e:
#         print(f"Error: {e}")
#     finally:
#         conn.close()
#         server_socket.close()

# if __name__ == '__main__':
#     start_server()

class ServerSocket():
    def __init__(self):
        self.SERVER_HOST = "0.0.0.0"
        self.SERVER_PORT = 12345
        
        self.server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server_socket.bind((self.SERVER_HOST,self.SERVER_PORT))
        self.server_socket.listen()
        
        print(f"Server listening on {self.SERVER_HOST}:{self.SERVER_PORT}")
        
        self.conn , self.addr = None , None
        self.connected = False
        
        connect_func = threading.Thread(target = self.wait_for_connection)
        connect_func.daemon = True
        connect_func.start()
        
    def wait_for_connection(self):
        
        self.conn , self.addr = self.server_socket.accept()

        print(f"Connected by {self.addr}")
        self.connected = True
        
        
    def __del__(self):
        self.conn.close()
        self.server_socket.close()
        
        print("--- CLOSED SERVER ---")
        

if __name__ == "__main__":
    
    server = ServerSocket()
    
    flag = True
    try:
        while True:
            if server.connected and flag:
                print("connected to client")
                flag = False
    except KeyboardInterrupt:
        pass