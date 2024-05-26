# update linux-steamdeck-zfs-bin when bumping
# also bump update.py
pkgname = "linux-steamdeck"
pkgver = "6.5.0"
pkgrel = 0
_vver = 7
archs = ["x86_64"]
make_dir = "build"
hostmakedepends = ["base-kernel-devel"]
depends = ["base-kernel"]
provides = ["linux"]
pkgdesc = f"Linux kernel for Steam Deck {pkgver[0:pkgver.rfind('.')]}.x"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://gitlab.com/evlaV/linux-integration"
source = f"{url}/-/archive/{pkgver}-valve{_vver}/linux-integration-{pkgver}-valve{_vver}.tar.gz"
sha256 = "bf026a1bc6835f8ad7de1854189509e979232892064e936665bd591024404318"
# no meaningful checking to be done
options = [
    "!check",
    "!debug",
    "!strip",
    "!scanrundeps",
    "!scanshlibs",
    "!linkparallel",
    "!lto",
    "textrels",
    "execstack",
    "foreignelf",  # vdso32
]

_flavor = "valve"

if self.profile().cross:
    broken = "linux-devel does not come out right"


def init_configure(self):
    from cbuild.util import linux

    linux.generate_scriptlets(self, _flavor)


def do_configure(self):
    from cbuild.util import linux

    linux.configure(self, _flavor)


def do_build(self):
    from cbuild.util import linux

    linux.build(self, _flavor)


def do_install(self):
    from cbuild.util import linux

    linux.install(self, _flavor)


@subpackage("linux-steamdeck-devel")
def _devel(self):
    self.depends += ["clang"]
    self.options = ["foreignelf", "execstack", "!scanshlibs"]
    return ["usr/src", "usr/lib/modules/*/build"]


@subpackage("linux-steamdeck-dbg")
def _dbg(self):
    self.pkgdesc += " (debug files)"
    self.options = [
        "!scanrundeps",
        "!strip",
        "!scanshlibs",
        "foreignelf",
        "execstack",
        "textrels",
    ]
    return ["usr/lib/debug", "boot/System.map-*"]
