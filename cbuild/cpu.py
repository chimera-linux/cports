import fnmatch
import platform
import sys

def init(host):
    global _host, _target
    _host = host
    _target = host

def init_target(profile):
    global _target, _target_wsize, _target_endian
    _target = profile.arch
    _target_wsize = profile.wordsize
    _target_endian = profile.endian

def target():
    return _target

def host():
    return _host

def target_endian():
    return _target_endian

def host_endian():
    return sys.byteorder

def target_wordsize():
    return _target_wsize

def host_wordsize():
    return int(platform.architecture()[0][:-3])

def match_arch(archn, *args):
    odd = True
    match = False
    for v in args:
        if odd:
            match = fnmatch.fnmatchcase(archn, v)
            odd = not odd
        else:
            if match:
                if callable(v):
                    return v(archn)
                return v
            else:
                odd = not odd
                continue
    return match

def match_target(*args):
    return match_arch(target(), *args)

def match_host(*args):
    return match_arch(host(), *args)
