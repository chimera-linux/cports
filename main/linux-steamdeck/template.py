# also bump update.py
pkgname = "linux-steamdeck"
pkgver = "6.5.0"
pkgrel = 6
_vver = 19
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
sha256 = "15cb3da0e81cd3cd3a3f899140d51d59aef16a53e42c0e9092ab2af6250e5405"
# no meaningful checking to be done
options = [
    "!check",
    "!debug",
    "!strip",
    "!scanrundeps",
    "!scanshlibs",
    "!lto",
    "textrels",
    "execstack",
    "foreignelf",  # vdso32
]

_flavor = "valve"

if self.current_target == "custom:generate-configs":
    hostmakedepends += ["base-cross", "ncurses-devel"]

if self.profile().cross:
    broken = "linux-devel does not come out right"


@custom_target("generate-configs", "patch")
def _(self):
    from cbuild.util import linux

    linux.update_configs(self, archs, _flavor)


def init_configure(self):
    from cbuild.util import linux

    linux.generate_scripts(self, _flavor)


def configure(self):
    from cbuild.util import linux

    linux.configure(self, _flavor)


def build(self):
    from cbuild.util import linux

    linux.build(self, _flavor)


def install(self):
    from cbuild.util import linux

    linux.install(self, _flavor)


@subpackage("linux-steamdeck-devel")
def _(self):
    self.depends += ["clang"]
    self.options = ["foreignelf", "execstack", "!scanshlibs"]
    return ["usr/src", "usr/lib/modules/*/build"]


@subpackage("linux-steamdeck-dbg")
def _(self):
    self.options = [
        "!scanrundeps",
        "!strip",
        "!scanshlibs",
        "foreignelf",
        "execstack",
        "textrels",
    ]
    return ["usr/lib/debug", "boot/System.map-*"]
