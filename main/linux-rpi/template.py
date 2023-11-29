# update linux-rpi-zfs-bin when bumping
pkgname = "linux-rpi"
pkgver = "6.1.63"
pkgrel = 0
archs = ["aarch64"]
make_dir = "build"
# necessary for efistub
make_env = {"CBUILD_BYPASS_STRIP_WRAPPER": "1"}
_commit = "cbc65d9c95088d1437a5a84c7d6628b8d27a86f1"
hostmakedepends = ["base-kernel-devel"]
depends = ["base-kernel"]
provides = ["linux"]
pkgdesc = (
    f"Linux kernel for Raspberry Pi 3 and 4 ({pkgver[0:pkgver.rfind('.')]}.x)"
)
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://github.com/raspberrypi/linux"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "abd3e993371206afcb21eb409c7b1f7d8b1f228ebf61e07b77cac6be7545bc9f"
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

_flavor = "rpi"

if self.profile().cross:
    broken = "linux-devel does not come out right"


def init_configure(self):
    # generate scriptlets for packaging, just hooking to base-kernel helpers
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


@subpackage("linux-rpi-devel")
def _devel(self):
    self.depends += ["clang"]
    self.options = ["foreignelf", "execstack", "!scanshlibs"]
    return ["usr/src", "usr/lib/modules/*/build"]


@subpackage("linux-rpi-dbg")
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
