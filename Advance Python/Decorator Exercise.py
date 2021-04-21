user1 = {
    'name': 'Sorna',
    'valid': True
}


def authenticated(fn):
    def wrapFunction(user):
        if dict(user)['valid'] == True:
            fn(user)

    return wrapFunction


def authenticate(fn):
    def wrapFunction(*args, **kwargs):
        if args[0]['valid'] == True:
            fn(*args, **kwargs)

    return wrapFunction


@authenticate
def message_friends(user):
    print("Message has been sent")


message_friends(user1)
