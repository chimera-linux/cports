def init(host):
    global _host, _target
    _host = host
    _target = host

def init_target(profile):
    global _target
    _target = profile.arch

def target():
    return _target

def host():
    return _host
