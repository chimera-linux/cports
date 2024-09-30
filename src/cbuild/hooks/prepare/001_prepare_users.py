# prepares /etc/passwd and /etc/group as needed to generate packages

from cbuild.core import chroot, paths

import shutil


def invoke(pkg):
    # don't involve users during bootstrap
    if pkg.stage < 1:
        return

    if not (pkg.template_path / "sysusers.conf").exists():
        return

    # assert this, should always be true...
    if not (paths.bldroot() / "usr/bin/sd-sysusers").exists():
        pkg.error("sd-sysusers not present in chroot")

    bp = paths.bldroot() / "usr/lib/sysusers.d"
    bp.mkdir(exist_ok=True)
    shutil.copyfile(pkg.template_path / "sysusers.conf", bp / "cbuild.conf")

    # delete potential shadow so sysusers does not fail
    (paths.bldroot() / "etc/shadow").unlink(missing_ok=True)

    chroot.enter("sd-sysusers", check=True)
