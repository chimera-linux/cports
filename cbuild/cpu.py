import fnmatch

def init(host, target):
    global _host, _target
    _host = host
    _target = target

def target():
    return _target

def host():
    return _host

def target_endian():
    return "little"

def host_endian():
    return "little"

def target_wordsize():
    return 64

def host_wordsize():
    return 64

def _match_arch(archn, *args):
    odd = True
    match = False
    for v in args:
        if odd:
            match = fnmatch.fnmatchcase(archn, v)
            odd = not odd
        else:
            if match:
                return v(archn)
            else:
                odd = not odd
                continue

def match_target(*args):
    return _match_arch(target(), *args)

def match_host(*args):
    return _match_arch(host(), *args)
