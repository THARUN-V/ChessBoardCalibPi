from ParseArgsFromCli import ParseArgs
from pi_client import SocketClient
from host_server import SocketServer

class ChessBoardCamCalib(ParseArgs):
    
    def __init__(self):
        ParseArgs.__init__(self)
        
        SocketServer.__init__(self)
        SocketClient.__init__(self)
        
        if self.args.server:
            self.run_server()
        if self.args.client:
            self.run_client()

if __name__ == "__main__":
    
    # params = ParseArgs()
    
    # print(params.args.server)
    
    chess_board_calib = ChessBoardCamCalib()
    