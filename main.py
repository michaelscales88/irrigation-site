if __name__ == '__main__':
    """
    Start the server by running:
    python main.py 8080 development.cfg
    """
    import sys
    from server import create_server
    port = sys.argv[1]
    args = sys.argv[1:]
    server = create_server(*args)
    server.run(port=int(port))

