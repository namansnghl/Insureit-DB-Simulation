import argparse, shlex


class CustomParsers:
    def __init__(self):
        self.parser = argparse.ArgumentParser()

    def _create_parser(self):
        raise NotImplementedError("Subclasses must implement the create_parser class method")

    def show_help(self):
        self.parser.print_help()
        print("Use '--help' for more information.")

    def parse(self, user_input: str = None):
        if not user_input:
            self.show_help()
        else:
            parts = shlex.split(user_input)
            try:
                return self.parser.parse_args(parts)
            except:
                self.show_help()


class CustomerParser(CustomParsers):
    def __init__(self):
        super().__init__()
        self.subparser = self.parser.add_subparsers(dest='client', title='Available customer operations')
        self._create_parser()

    def _create_parser(self):
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
        menu.add_argument('--email', help="Change your Email ID", action="store_true")
        menu.add_argument('--phone', help="Change your Phone Number", action="store_true")
        menu.add_argument('--address', help="Change your Address", action="store_true")

    def _buy_new(self):
        buy = self.subparser.add_parser('buy', help="Purchase a new policy")
        buy.add_argument('--show-auto', help="Show only Auto Policies offered", default=False, action="store_true")
        buy.add_argument('--show-home', help="Show only Home Policies offered", default=False, action="store_true")

    def _claim(self):
        claim = self.subparser.add_parser('claim', help="Manage your claims or create new")
        claim.add_argument('--view', action='store_true', help="Show all claims")
        # claim.add_argument('--status', help="Check claim status")
        claim.add_argument('-n', '--new', action='store_true', help="Start a new claim")


class AgentParser(CustomParsers):
    def __init__(self):
        super().__init__()
        self.subparser = self.parser.add_subparsers(dest='agent', title='Available Agent operations')
        self._create_parser()

    def _create_parser(self):
        self._cust()
        self._policy()

    def _cust(self):
        cust = self.subparser.add_parser('client', help='Manage your customer')
        cust.add_argument('-n', '--new', action='store_true', help="Register new client")
        cust.add_argument("--show", action='store_true', help="Display all clients under you")

    def _policy(self):
        pol = self.subparser.add_parser('policy', help="Perform policy related Operations")
        pol.add_argument('--at-risk', action='store_true', help="Show clients with policy terms at risk")
        pol.add_argument('--calc-premium', action='store_true', help="Calculate policy premium for a potential client")


class RootParser(CustomParsers):
    def __init__(self):
        super().__init__()
        self.subparser = self.parser.add_subparsers(dest='root', title='Available Administrator operations')
        self._create_parser()

    def _create_parser(self):
        self._agent()
        self._claims()

    def _agent(self):
        a = self.subparser.add_parser('agent', help='Manage agents')
        a.add_argument('-n', '--new', action='store_true', help="Register new agent")
        a.add_argument("--performance", action='store_true', help="Display all agents performance")

    def _claims(self):
        a = self.subparser.add_parser('claims', help='Manage claims')
        a.add_argument('-p', '--pending', action='store_true', help="Show pending claims")
        a.add_argument('-a', '--approved', action='store_true', help="show approved claims")
