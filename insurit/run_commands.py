from .backend.user_management import userType


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

def run_admin(args, **kwargs):
    ...
