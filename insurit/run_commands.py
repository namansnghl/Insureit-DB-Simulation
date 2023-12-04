from .backend.user_management import userType
from .backend.views import *
from .backend.utils import *
from .backend.finance import *
from .backend.account_info import chsettings
from .backend.forms import *
from .backend.analytics import *


def run_command(args, **kwargs):
    access_lvl = kwargs['access_lvl']
    if access_lvl == 1:
        run_agent(args, **kwargs)
    elif access_lvl == 2:
        run_cust(args, **kwargs)
    else:
        run_admin(args, **kwargs)


def run_cust(args, **kwargs):
    if args.client == 'pay':
        pay_policy(kwargs['conn'], kwargs['id'])

    elif args.client == 'my-policies':
        view_policy(kwargs['conn'], kwargs['id'])

    elif args.client == 'account-settings':
        if args.email:
            chsettings(kwargs['conn'], kwargs['id'], option=1)
        elif args.address:
            chsettings(kwargs['conn'], kwargs['id'], option=3)
        elif args.phone:
            chsettings(kwargs['conn'], kwargs['id'], option=2)
        else:
            chsettings(kwargs['conn'], kwargs['id'])

    elif args.client == 'buy':
        ...

    elif args.client == 'claim':
        if args.new:
            create_new_claim(kwargs['conn'])
        if args.view:
            viewClaims(kwargs['conn'], kwargs['id'])


def run_agent(args, **kwargs):
    if args.agent == 'client':
        if args.new:
            userType(kwargs['conn'], kwargs['access_lvl'])
        if args.show:
            showCustomers(kwargs['conn'], kwargs['id'])
    elif args.agent == 'policy':
        if args.calc_premium:
            calculate_premium(kwargs['conn'])
        if args.at_risk:
            check_due_dates(kwargs['conn'])


def run_admin(args, **kwargs):
    if args.root == 'agent':
        if args.new:
            userType(kwargs['conn'], kwargs['access_lvl'])
        elif args.performance:
            agentPerformance(connection=kwargs['conn'])

    elif args.root == 'pending-claim':
        pendingClaims(kwargs['conn'])
