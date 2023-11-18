import argparse
import shlex
from .backend import authenticate as auth
from .backend.db_manager import Connection

connection = None


def run(app: str, conn):
    global connection
    connection = conn
    login_command = 'login'

    print("Application Starting\n WELCOME TO INSURIT - YOUR TRUSTED INSURANCE PROVIDER")
    loginparser = argparse.ArgumentParser()
    subparsers = loginparser.add_subparsers(dest="command", metavar='')

    # Subcommand: login
    login_parser = subparsers.add_parser(login_command, help="Login to Insureit")
    login_parser.add_argument("-u", "--username", help="Your Insureit login username", required=True)
    login_parser.add_argument("-p", "--password", help="Your Insureit login password", required=True)

    while True:
        user_input = input(f"\n{app}> ")

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
            if args.command == login_command:
                if auth.login(args.username, args.password):
                    print("Authentication successful.\nWelcome ", args.username)
                    if loggedin(app, args.username):
                        user_input = 'exit'
                else:
                    print("Authentication failed. Incorrect Username/Password.")

        if user_input.strip().lower() in ['exit', 'cancel', 'disconnect']:
            Connection.disconnect(conn)
            print("Connection closed, Exiting...")
            break


def loggedin(app: str, username: str) -> int:
    global connection
    parser = argparse.ArgumentParser(description="Your script description")
    # Add argparse commands

    while True:
        user_input = input(f"{app} {username}> ")

        if user_input.lower() == 'exit':
            break
        if user_input.lower() == 'logout':
            print("Logging you out...\n")
            return 0

        print(f"Running command: {user_input}")

    return 1


def unknown_command(parser):
    parser.print_help()
    print("Please provide a subcommand. Use 'insureit --help' for more information.")