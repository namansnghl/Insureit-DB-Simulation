import argparse
from authenticate import login
import user_commands


def get_authentication_parser():
	parser = argparse.ArgumentParser(description="Authentication and command execution script")
	parser.add_argument("-u", "--username", help="Username")
	parser.add_argument("-p", "--password", help="Password")
	return parser.parse_args()

if __name__ == "__main__":
	
	args = get_authentication_parser()

	if args.username and args.password:
		if login(args.username, args.password):
			print("Authentication successful.")
			user_commands.run(args.username)
		else:
			print("Authentication failed.")
	else:
		print("Please provide both username and password.")
