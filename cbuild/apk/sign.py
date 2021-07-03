from cbuild.core import logger, paths

import os
import io
import gzip
import time
import getpass
import pathlib
import tarfile
import subprocess

from . import util

def _get_keypath(keypath):
    keypath = pathlib.Path(keypath)

    if keypath.is_absolute():
        return keypath

    if keypath.parent == pathlib.Path():
        # just a filename
        return paths.distdir() / "etc" / "keys" / keypath
    else:
        # otherwise a path relative to distdir
        return paths.distdir() / keypath

# returns the compressed signature data given
# either an input file path or raw input bytes
def sign(keypath, data, epoch):
    if isinstance(data, bytes):
        inparg = []
        inpval = data
    else:
        inparg = [str(data)]
        inpval = None

    keypath = _get_keypath(keypath)

    if not keypath.is_file():
        logger.get().out_red(f"Non-existent private key '{keypath}'")
        raise Exception()

    keyname = keypath.name + ".pub"
    signame = ".SIGN.RSA." + keyname

    sout = subprocess.run([
        "openssl", "dgst", "-sha1", "-sign", str(keypath), "-out", "-"
    ] + inparg, input = inpval, capture_output = True)

    if sout.returncode != 0:
        logger.get().out_red("Signing failed!")
        logger.get().out_plain(sout.stderr.strip().decode())
        raise Exception()

    sigio = io.BytesIO()
    rawdata = sout.stdout

    with tarfile.open(None, "w", fileobj = sigio) as sigtar:
        tinfo = tarfile.TarInfo(signame)
        tinfo.size = len(rawdata)
        tinfo.mtime = int(epoch)
        tinfo.uname = "root"
        tinfo.gname = "root"
        tinfo.uid = 0
        tinfo.gid = 0
        with io.BytesIO(rawdata) as sigstream:
            sigtar.addfile(tinfo, sigstream)

    cval = gzip.compress(
        util.strip_tar_endhdr(sigio.getvalue()), mtime = int(epoch)
    )

    sigio.close()
    return cval

def keygen(keypath, size = 2048):
    pass

    if not keypath:
        # does not have to succeed, e.g. there may not even be git at all
        eaddr = subprocess.run(
            ["git", "config", "--get", "user.email"], capture_output = True
        )
        if eaddr.returncode == 0:
            eaddr = eaddr.stdout.strip().decode()
            if len(eaddr) == 0:
                eaddr = None
        else:
            eaddr = None
        if not eaddr:
            keyn = getpass.getuser()
        else:
            keyn = eaddr
        keypath = keyn + "-" + hex(int(time.time()))[2:] + ".rsa"
        logger.get().warn(f"No key path provided, using '{keypath}'")

    keypath = _get_keypath(keypath)

    os.makedirs(keypath.parent, exist_ok = True)

    if keypath.is_file():
        logger.get().out_red("Attempt to overwrite an existing key, aborting")
        raise Exception()

    kout = subprocess.run([
        "openssl", "genrsa", "-out", str(keypath), str(size)
    ], umask = 0o007)

    if not kout.returncode == 0:
        logger.get().out_red("Key generation failed")
        raise Exception()

    pout = subprocess.run([
        "openssl", "rsa", "-in", str(keypath),
        "-pubout", "-out", str(keypath) + ".pub"
    ])

    if not pout.returncode == 0:
        logger.get().out_red("Public key generation failed")
        raise Exception()

    logger.get().out("Key successfully generated.")
    logger.get().out("In order to use it, add it to your 'etc/config.ini':")
    logger.get().out_plain("""
[signing]
key = KEYPATH # absolute path, relative path to cports or filename in etc/keys
""")
