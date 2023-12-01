
def run(args, access_lvl: int, **kwargs):
    print(f"Running command: {args}")

    if access_lvl == 1:
        run_agent(args, **kwargs)
    elif access_lvl == 2:
        run_cust(args, **kwargs)
    else:
        run_admin(args, **kwargs)


def run_cust(args, **kwargs):
    ...


def run_agent(args, **kwargs):
    ...


def run_admin(args, **kwargs):
    ...
