import argparse

class ParseArgs:
    
    def __init__(self):
        # Create the parser
        self.parser = argparse.ArgumentParser(description = "A script to calibrate camera for fisheye effect elimation using chessboard.")
        self.parser.add_argument("--server",
                                 action = "store_true",
                                 help = "param to set as server to receive images and perform calibration.")
        self.parser.add_argument("--client",
                                 action = "store_true",
                                 help = "param to set as client for capturing images from pi and send to server for processing.")
        # Parse the arguments
        self.args = self.parser.parse_args()

