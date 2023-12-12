import argparse, shlex


# Parent class to all the parsers - agent, client and admin
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
        """
        Adds all the sub parsers to the main parser
        :return: None
        """
        self._premium_pay()
        self._policy_view()
        self._edit_acct()
        # self._buy_new()
        self._claim()

    def _premium_pay(self):
        """
        Customer pay premium for policy
        :return: None
        """
        self.subparser.add_parser('pay', help='Make premium payment towards policy')

    def _policy_view(self):
        """
        Customer manages the policies he/she/they own
        :return:None
        """
        view_pol = self.subparser.add_parser('my-policies', help='Display policies you own or have owned in past')
        view_pol.add_argument('--auto', action="store_true",
                              help="Show only Auto Policies", default=False)
        view_pol.add_argument('--home', action="store_true",
                              help="Show only Home Policies", default=False)

    def _edit_acct(self):
        """
        Customer changes their account information
        :return: None
        """
        menu = self.subparser.add_parser('account-settings', help="Manage Account Settings and Information")
        menu.add_argument('--email', help="Change your Email ID", action="store_true")
        menu.add_argument('--phone', help="Change your Phone Number", action="store_true")
        menu.add_argument('--address', help="Change your Address", action="store_true")

    # def _buy_new(self):
    #     buy = self.subparser.add_parser('buy', help="Purchase a new policy")
    #     buy.add_argument('--show-auto', help="Show only Auto Policies offered", default=False, action="store_true")
    #     buy.add_argument('--show-home', help="Show only Home Policies offered", default=False, action="store_true")

    def _claim(self):
        """
        Customer creates a claim
        :return: None
        """
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
        """
        Adds all the sub parsers to the main parser
        :return: None
        """
        self._cust()
        self._policy()

    def _cust(self):
        """
        Agent does Customer creation and view
        :return: None
        """
        cust = self.subparser.add_parser('client', help='Manage your customer')
        cust.add_argument('-n', '--new', action='store_true', help="Register new client")
        cust.add_argument("--show", action='store_true', help="Display all clients under you")

    def _policy(self):
        """
        Agent manages policies
        :return: None
        """
        pol = self.subparser.add_parser('policy', help="Perform policy related Operations")
        pol.add_argument('--add-new', action='store_true', help="Add new Policy to Insurit")
        pol.add_argument('--at-risk', action='store_true', help="Show clients with policy terms at risk")
        pol.add_argument('--calc-premium', action='store_true', help="Calculate policy premium for a potential client")


class RootParser(CustomParsers):
    def __init__(self):
        super().__init__()
        self.subparser = self.parser.add_subparsers(dest='root', title='Available Administrator operations')
        self._create_parser()

    def _create_parser(self):
        """
        Adds all the sub parsers to the main parser
        :return: None
        """
        self._agent()
        self._claims()
        self._dbs()

    def _agent(self):
        """
        Admin manages agents
        :return: None
        """
        a = self.subparser.add_parser('agent', help='Manage agents')
        a.add_argument('-n', '--new', action='store_true', help="Register new agent")
        a.add_argument("--performance", action='store_true', help="Display all agents performance")

    def _claims(self):
        """
        Admin manages claims
        :return: None
        """
        a = self.subparser.add_parser('claims', help='Manage claims')
        a.add_argument('-p', '--pending', action='store_true', help="Show pending claims")
        a.add_argument('-a', '--approved', action='store_true', help="show approved claims")

    def _dbs(self):
        """
        Admin resets the database
        :return: None
        """
        a = self.subparser.add_parser("database", help="Manage Database setup")
        a.add_argument("--reset", help="Reset tables to initial", required=True)