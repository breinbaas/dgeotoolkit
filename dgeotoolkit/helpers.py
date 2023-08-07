import inspect


def _next_id(c, next_id=-1):
    for member, value in c.__dict__.items():
        if member == "Id":
            next_id = int(member)
        if type(value) == list:
            for e in value:
                _next_id(value, next_id)
        if inspect.isclass(value):
            _next_id(value, next_id)
