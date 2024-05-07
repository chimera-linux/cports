# update linux-rpi-zfs-bin when bumping
pkgname = "linux-rpi"
pkgver = "6.6.30"
pkgrel = 0
archs = ["aarch64"]
make_dir = "build"
# necessary for efistub
make_env = {"CBUILD_BYPASS_STRIP_WRAPPER": "1"}
_commit = "1e53604087930e7cf42eee3d42572d0d6f54c86a"
hostmakedepends = ["base-kernel-devel"]
depends = ["base-kernel"]
provides = ["linux"]
pkgdesc = (
    f"Linux kernel for Raspberry Pi 3/4/5 ({pkgver[0:pkgver.rfind('.')]}.x)"
)
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://github.com/raspberrypi/linux"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "9c895d088e569987bd9db69f6c0ab0a5b4dd0ed7f7745520b67acf4d3d9248e9"
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
