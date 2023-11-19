import argparse, shlex


class CustomParsers:
    def __init__(self):
        self.parser = argparse.ArgumentParser()

    def create_parser(self):
        raise NotImplementedError("Subclasses must implement the create_parser class method")

    def show_help(self):
        self.parser.print_help()
        print("Use '--help' for more information.")

    def parse(self, user_input: str):
        parts = shlex.split(user_input)
        try:
            return self.parser.parse_args(parts)
        except:
            self.show_help()


class CustomerParser(CustomParsers):
    def __init__(self):
        super().__init__()
        self.subparser = self.parser.add_subparsers(dest='customer', help='Parse customer commands')
        self.__create_parser()

    def __create_parser(self):
        self._premium_pay()
        self._policy_view()
        self._edit_acct()
        self._buy_new()
        self._claim()

    def _premium_pay(self):
        self.subparser.add_parser('pay', help='Make premium payment towards policy')

    def _policy_view(self):
        view_pol = self.subparser.add_parser('my-policies', help='Display policies you own or have owned in past')
        view_pol.add_argument('--auto', action="store_true",
                              help="Show only Auto Policies", default=False)
        view_pol.add_argument('--home', action="store_true",
                              help="Show only Home Policies", default=False)

    def _edit_acct(self):
        menu = self.subparser.add_parser('account-settings', help="Manage Account Settings and Information")
        menu.add_argument('--ch-pass', help="Change your password")
        menu.add_argument('--ch-usr', help="Change your username")
        # TODO Add more options

    def _buy_new(self):
        buy = self.subparser.add_parser('buy', help="Purchase a new policy")
        buy.add_argument('--show-auto', help="Show only Auto Policies offered", default=False, action="store_true")
        buy.add_argument('--show-home', help="Show only Home Policies offered", default=False, action="store_true")

    def _claim(self):
        claim = self.subparser.add_parser('claim', help="Manage your claims or create new")
        claim.add_argument('--view', help="Show all claims")
        claim.add_argument('--status', help="Check claim status")
        claim.add_argument('-n', '--new', help="Start a new claim")


class AgentParser(CustomParsers):
    def __init__(self):
        super().__init__()

    def create_parser(self):
        ...


class RootParser(CustomParsers):
    def __init__(self):
        super().__init__()

    def create_parser(self):
        ...
