import fnmatch
import platform
import sys

def init(host, target):
    global _host, _target
    _host = host
    _target = target

def init_target(wordsize, endian):
    global _target_wsize, _target_endian
    _target_wsize = wordsize
    _target_endian = endian

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

def _match_arch(archn, *args):
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
    return _match_arch(target(), *args)

def match_host(*args):
    return _match_arch(host(), *args)
