if __name__ == '__main__':
    import sys
    from server import create_server
    port = sys.argv[1]
    args = sys.argv[2:]
    server = create_server(*args)
    server.run(port=int(port))
