import argparse

def run(username):
	parser = argparse.ArgumentParser(description="Your script description")
	# Add argparse commands

	while True:
		user_input = input(f"{username}$ ")

		if user_input.lower() == 'exit':
			print("Exiting...")
			break

		print(f"Running command: {user_input}")