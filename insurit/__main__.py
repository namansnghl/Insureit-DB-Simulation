import argparse
import insurit.app as app
from .backend.db_manager import Connection


def main():
    app_name = "insurit"
    start_service = "connect"
    parser = argparse.ArgumentParser(
        prog=app_name,
        description="Insurance Provider Application",
        epilog="Example usage: insureit connect -u <username> --hostname <host>"
    )

    subparsers = parser.add_subparsers(dest="command", title="To start the Insurit Application", metavar='')

    # Subcommand: start service
    service_parser = subparsers.add_parser(start_service, help="Connect to remote DB")
    service_parser.add_argument('--hostname', metavar='<hostname>', help="Host of the Insurit service")
    service_parser.add_argument('--port', metavar='<port>', help="Port number to connect with service")
    service_parser.add_argument('-u','--username', metavar='<username>', help="Username to access the service")

    args = parser.parse_args()

    # if asked to connect db
    if args.command == start_service:
        connector = Connection(hostname=args.hostname, port=args.port, username=args.username)
        connector.fetch_creds()
        conn = connector.connect()
        if conn:
            app.run(app_name, conn)
    else:
        app.unknown_command(parser)


if __name__ == "__main__":
    main()
