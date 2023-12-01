import argparse
import shlex
from .backend import authenticate as auth
from .backend.db_manager import Connection
from .parsers import CustomerParser, AgentParser, RootParser

connection = None


def run(app: str, conn):
    global connection
    connection = conn
    login_command = 'login'
    login_agent = 'agent'
    login_root = 'root'
    levels = {login_command: 2, login_agent: 1, login_root: 0}

    print("Application Starting\n WELCOME TO INSURIT - YOUR TRUSTED INSURANCE PROVIDER")
    loginparser = argparse.ArgumentParser()
    subparsers = loginparser.add_subparsers(dest="command", metavar='')

    # Subcommand: login
    login_parser = subparsers.add_parser(login_command, help="Login to Insureit")
    login_parser.add_argument("-u", "--username", help="Your Insureit login username", required=True)
    login_parser.add_argument("-p", "--password", help="Your Insureit login password", required=True)
    # Subcommand: agent
    login_parser = subparsers.add_parser(login_agent, help="Agent login to Insureit")
    login_parser.add_argument("-u", "--username", help="Insureit login username", required=True)
    login_parser.add_argument("-p", "--password", help="Insureit login password", required=True)
    # Subcommand: root
    login_parser = subparsers.add_parser(login_root, help="Administrator login to Insureit")
    login_parser.add_argument("-u", "--username", help="Insureit login username", required=True)
    login_parser.add_argument("-p", "--password", help="Insureit login password", required=True)

    while True:
        user_input = input(f"\n{app}> ")
        if not user_input:
            continue
        if user_input.strip().lower() in ['exit', 'cancel', 'disconnect']:
            Connection.disconnect(conn)
            print("Connection closed, Exiting...")
            break

        parts = shlex.split(user_input)
        # handle package name if parsed (we don't need package name anymore)
        if parts[0].lower() == 'insurit':
            if len(parts) != 1:
                parts = parts[1:]
            else:
                unknown_command(loginparser)

        try:
            args = loginparser.parse_args(parts)
        except:
            unknown_command(loginparser)
        else:
            if auth.login(conn.cursor(), args.username, args.password, levels[args.command]):
                print("Authentication successful.\nWelcome ", args.username)
                if loggedin(app, args.username, levels[args.command]):
                    user_input = 'exit'
            else:
                print("Authentication failed. Incorrect Username/Password.")

        if user_input.strip().lower() in ['exit', 'cancel', 'disconnect']:
            Connection.disconnect(conn)
            print("Connection closed, Exiting...")
            break


def loggedin(app: str, username: str, access: int) -> int:
    global connection
    access_levels = [RootParser, AgentParser, CustomerParser]
    parser = access_levels[access]()
    id = auth.id_from_username(connection, access, username)

    while True:
        user_input = input(f"{app} {username}> ")
        if not user_input:
            continue
        if user_input in ['-h', '--help']:
            parser.show_help()
            continue
        if user_input.lower().strip() == 'exit':
            break
        if user_input.lower().strip() == 'logout':
            print("Logging you out...\n")
            return 0

        args = parser.parse(user_input)

        print(f"Running command: {user_input}")

    return 1


def unknown_command(parser):
    parser.print_help()
    print("Please provide a subcommand. Use 'insureit --help' for more information.")
