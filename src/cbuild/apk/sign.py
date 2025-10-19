from cbuild.core import logger, paths, errors, git

import re
import time
import shutil
import getpass
import pathlib
import subprocess

_keypath = None


def register_key(keypath):
    global _keypath

    if not keypath:
        _keypath = None
        return

    keypath = pathlib.Path(keypath).expanduser()

    if keypath.is_absolute():
        _keypath = keypath
        return

    if keypath.parent == pathlib.Path():
        # just a filename
        _keypath = paths.distdir() / "etc" / "keys" / keypath
    else:
        # otherwise a path relative to distdir
        _keypath = paths.distdir() / keypath


def get_keypath():
    return _keypath


def keygen(size, eaddr, cfgfile, cfgpath):
    if not shutil.which("openssl"):
        raise errors.CbuildException("openssl is missing")

    keypath = get_keypath()

    if not keypath or eaddr:
        if not eaddr:
            eaddr = git.call(["config", "--get", "user.email"], gitconfig=True)
            if eaddr is not None:
                eaddr = eaddr.strip().decode()
                if len(eaddr) == 0:
                    eaddr = None
        if not eaddr:
            keyn = getpass.getuser()
        else:
            keyn = eaddr
        register_key(keyn + "-" + hex(int(time.time()))[2:] + ".rsa")
        keypath = get_keypath()
        logger.get().out(
            f"\f[orange]WARNING: No key path provided, using '{keypath}'"
        )

    keypath.parent.mkdir(parents=True, exist_ok=True)

    if keypath.is_file():
        raise errors.CbuildException("attempt to overwrite an existing key")

    kout = subprocess.run(
        ["openssl", "genrsa", "-out", keypath, str(size)], umask=0o007
    )

    if not kout.returncode == 0:
        raise errors.CbuildException("key generation failed")

    pout = subprocess.run(
        [
            "openssl",
            "rsa",
            "-in",
            keypath,
            "-pubout",
            "-out",
            str(keypath) + ".pub",
        ]
    )

    if not pout.returncode == 0:
        raise errors.CbuildException("public key generation failed")

    logger.get().out("Key successfully generated.")

    if "signing" in cfgfile and "key" in cfgfile["signing"]:
        if cfgfile["signing"]["key"] != cfgpath:
            logger.get().out("Signing key set in config, but not the same.")
            logger.get().out("You will probably need to update it.")
        else:
            logger.get().out("The key was already found in the config file.")
        return

    logger.get().out("Updating configuration file...")

    rkpath = keypath
    if rkpath.is_relative_to(paths.distdir() / "etc" / "keys"):
        rkpath = rkpath.relative_to(paths.distdir() / "etc" / "keys")
    elif rkpath.is_relative_to(paths.distdir()):
        rkpath = rkpath.relative_to(paths.distdir())

    if "signing" in cfgfile:
        with open(cfgpath, "r") as cf:
            with open(cfgpath + ".new", "w") as ocf:
                for ln in cf:
                    ocf.write(ln)
                    if re.match(r"^\[signing\]", ln):
                        ocf.write(f"key = {rkpath}\n")

        pathlib.Path(cfgpath + ".new").rename(cfgpath)
    else:
        with open(cfgpath, "a") as cf:
            cf.write("\n[signing]\n")
            cf.write(f"key = {rkpath}\n")

    if not pout.returncode == 0:
        raise errors.CbuildException("public key generation failed")

    logger.get().out("Configuration file updated.")
