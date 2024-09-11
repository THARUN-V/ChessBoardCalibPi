from ParseArgsFromCli import ParseArgs


if __name__ == "__main__":
    
    params = ParseArgs()
    
    print(params.args.server)