from cbuild.core import logger, paths

import os
import time
import getpass
import pathlib
import subprocess

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
        if not eaddr:
            keyn = getpass.getuser()
        else:
            keyn = eaddr
        keypath = keyn + "-" + hex(int(time.time()))[2:]
        logger.get().warn(f"No key path provided, using '{keypath}'")

    keypath = pathlib.Path(keypath)

    if not keypath.is_absolute():
        if keypath.parent == pathlib.Path():
            # just a filename
            keypath = paths.distdir() / "etc" / "keys" / keypath
        else:
            # otherwise a path relative to distdir
            keypath = paths.distdir() / keypath

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
