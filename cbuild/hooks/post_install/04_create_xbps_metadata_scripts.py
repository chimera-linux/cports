from cbuild.core import logger, paths

import os
import shutil
import tempfile
import subprocess

def handle_scripts(pkg, action, path):
    tmpf = tempfile.TemporaryFile()
    tmpf.write(b"""#!/bin/sh
#
# Generic INSTALL/REMOVE script. Arguments passed to this script:
#
# \$1 = ACTION	[pre/post]
# \$2 = PKGNAME
# \$3 = VERSION
# \$4 = UPDATE	[yes/no]
# \$5 = CONF_FILE (path to xbps.conf)
# \$6 = ARCH (uname -m)
#
# Note that paths must be relative to CWD, to avoid calling
# host commands if /bin/sh (dash) is not installed and it's
# not possible to chroot(2).
#

export PATH="/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin"

TRIGGERSDIR="./usr/libexec/xbps-triggers"
ACTION="\$1"
PKGNAME="\$2"
VERSION="\$3"
UPDATE="\$4"
CONF_FILE="\$5"
ARCH="\$6"

#
# The following code will run the triggers.
#

""")

    if len(pkg.make_dirs) > 0:
        if not "mkdirs" in pkg.triggers:
            pkg.triggers.append("mkdirs")
        tmpf.write(b"export make_dirs=\"${make_dirs}\"\n")

    tmpf.write(b"\n")

    tdir = paths.templates() / "xbps-triggers" / "files"

    if len(pkg.triggers) > 0:
        tmpf.write(b"case \"${ACTION}\" in\n")
        tmpf.write(b"pre)\n")
        tgs = {}

        for f in pkg.triggers:
            if not (tdir / f).is_file():
                tmpf.close()
                pkg.error(f"unknown trigger {f}")
            logger.get().out_plain(
                f"   Added trigger '{f}' for the '{action.upper()}' script."
            )
            sp = subprocess.run(
                [str (tdir / f), "targets"], capture_output = True
            )
            tgs[f] = sp.stdout.strip().decode("ascii").split()

        for f in pkg.triggers:
            for tg in tgs[f]:
                if tg != "pre-" + action:
                    continue
                tmpf.write(f"\t${{TRIGGERSDIR}}/{f} run {tg} ${{PKGNAME}} ${{VERSION}} ${{UPDATE}} ${{CONF_FILE}}\n".encode())
                tmpf.write(b"\t[ $? -ne 0 ] && exit $?\n")

        tmpf.write(b"\t;;\n")
        tmpf.write(b"post)\n")

        for f in pkg.triggers:
            for tg in tgs[f]:
                if tg != "post-" + action:
                    continue
                tmpf.write(f"\t${{TRIGGERSDIR}}/{f} run {tg} ${{PKGNAME}} ${{VERSION}} ${{UPDATE}} ${{CONF_FILE}}\n".encode())
                tmpf.write(b"\t[ $? -ne 0 ] && exit $?\n")

        tmpf.write(b"\t;;\n")
        tmpf.write(b"esac\n\n")
    elif not path.is_file():
        tmpf.close()
        return

    if action == "install" or action == "remove":
        if path.is_file():
            tmpf.write(path.read_bytes())
        tmpf.write(b"\n")
        tmpf.write(b"exit 0\n")
        tmpf.seek(0)
        with open(pkg.destdir / action.upper(), "wb") as f:
            f.write(tmpf.read())
            tmpf.close()
        os.chmod(pkg.destdir / action.upper(), 0o755)

def invoke(pkg):
    if pkg.parent:
        # subpkg
        pkgbase = paths.templates() / pkg.parent.pkgname
        meta_install = pkgbase / (pkg.pkgname + ".INSTALL")
        msg_install = pkgbase / (pkg.pkgname + ".INSTALL.msg")
        meta_remove = pkgbase / (pkg.pkgname + ".REMOVE")
        msg_remove = pkgbase / (pkg.pkgname + ".REMOVE.msg")
    else:
        # sourcepkg
        pkgbase = paths.templates() / pkg.pkgname
        meta_install = pkgbase / "INSTALL"
        msg_install = pkgbase / "INSTALL.msg"
        meta_remove = pkgbase / "REMOVE"
        msg_remove = pkgbase / "REMOVE.msg"

    handle_scripts(pkg, "install", meta_install)
    handle_scripts(pkg, "remove", meta_remove)

    if msg_install.is_file():
        os.chmod(shutil.copy2(msg_install, pkg.destdir), 0o644)
    if msg_remove.is_file():
        os.chmod(shutil.copy2(msg_remove, pkg.destdir), 0o644)
