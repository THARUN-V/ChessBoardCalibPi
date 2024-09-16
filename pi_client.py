import socket
import threading
import time

class SocketClient:
    
    def __init__(self):
        
        self.CLIENT_HOST = "192.168.43.69"
        self.CLIENT_PORT = 12345
        
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.connected = False
        
        # Thread to establish connection with server
        connect_to_server_thread = threading.Thread(target = self.connect_to_server)
        connect_to_server_thread.daemeon = True
        connect_to_server_thread.start()
        
        # Thread to test connection by sending msg to server
        msg_thread = threading.Thread(target = self.send_msg)
        msg_thread.daemon = True
        msg_thread.start()
    
    def connect_to_server(self):
        """
        Function to establish connection with client.
        """
        while not self.connected:
            try:
                self.client_socket.connect((self.CLIENT_HOST,self.CLIENT_PORT))
                self.connected = True
            except ConnectionRefusedError:
                # print(f"***** Retrying connection to server ********")
                pass
            
            
        print("---- Connected to server -----")
        
    def send_msg(self):
        """
        Fucntion for testing connection , by transmittin data to server on succesfull connection.
        """
        
        while True:
            if self.connected:
                message = ":) Hi from client ..."
                self.client_socket.sendall(message.encode())
                print("- Message Sent To Server -")
                time.sleep(2)
        
    def __del__(self):
        self.client_socket.close()
        
        
if __name__ == "__main__":
    
    client = SocketClient()
    
    while True:
        # print(f"####### connect flag : {client.connected} ##############")
        pass