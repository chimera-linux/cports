# also bump update.py
pkgname = "linux-steamdeck"
pkgver = "6.8.12"
pkgrel = 1
_vver = 9
archs = ["x86_64"]
build_style = "linux-kernel"
configure_args = ["FLAVOR=valve", f"RELEASE={pkgrel}"]
make_dir = "build"
hostmakedepends = ["base-kernel-devel"]
depends = ["base-kernel"]
provides = ["linux"]
pkgdesc = f"Linux kernel for Steam Deck {pkgver[0 : pkgver.rfind('.')]}.x"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://gitlab.com/evlaV/linux-integration"
source = f"{url}/-/archive/{pkgver}-valve{_vver}/linux-integration-{pkgver}-valve{_vver}.tar.gz"
sha256 = "bebdbf059359a73c80c53838a77a89e7a2c2ab9b7decfc92fa134bd3b22110ba"
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

if self.current_target == "custom:generate-configs":
    hostmakedepends += ["base-cross", "ncurses-devel"]

if self.profile().cross:
    broken = "linux-devel does not come out right"


@subpackage("linux-steamdeck-devel")
def _(self):
    self.depends += ["clang"]
    self.options = ["foreignelf", "execstack", "!scanshlibs"]
    return ["usr/src", "usr/lib/modules/*/build"]


@subpackage("linux-steamdeck-dbg", self.build_dbg)
def _(self):
    self.options = [
        "!scanrundeps",
        "!strip",
        "!scanshlibs",
        "foreignelf",
        "execstack",
        "textrels",
    ]
    return ["usr/lib/debug", "usr/lib/modules/*/apk-dist/boot/System.map-*"]
