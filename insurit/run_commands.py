from .backend.user_management import userType
from .backend.views import *
from .backend.utils import *
from datetime import datetime, timedelta
from .backend.finance import *


def run_command(args, **kwargs):
    print(f"Running command: {args}")
    access_lvl = kwargs['access_lvl']
    if access_lvl == 1:
        run_agent(args, **kwargs)
    elif access_lvl == 2:
        run_cust(args, **kwargs)
    else:
        run_admin(args, **kwargs)


def run_cust(args, **kwargs):
    ...


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
    ...
