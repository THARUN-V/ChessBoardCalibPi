from ParseArgsFromCli import ParseArgs
from pi_client import SocketClient
from host_server import SocketServer

class ChessBoardCamCalib(ParseArgs):
    
    def __init__(self):
        
        ParseArgs.__init__(self)
        
        socket_server = SocketServer()
        socket_client = SocketClient()
        
        if self.args.server:
            socket_server.run_server()
        if self.args.client:
            socket_client.run_client()

if __name__ == "__main__":
    
    # params = ParseArgs()
    
    # print(params.args.server)
    
    chess_board_calib = ChessBoardCamCalib()
    