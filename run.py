if __name__ == '__main__':
    import sys

    from server import create_server
    from run_tests import TestUserModel
    port = sys.argv[1]
    args = sys.argv[2:]

    # Unit testing stuff
    # import unittest
    server = create_server(*args)
    # with server.app_context():
    #     unittest.main()
    server.run(port=int(port))

