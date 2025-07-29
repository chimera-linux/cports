# also bump update.py
pkgname = "linux-steamdeck"
pkgver = "6.11.11"
pkgrel = 0
_vver = 20
archs = ["x86_64"]
build_style = "linux-kernel"
configure_args = ["FLAVOR=valve", f"RELEASE={pkgrel}"]
make_dir = "build"
hostmakedepends = ["base-kernel-devel"]
depends = ["base-kernel"]
provides = ["linux"]
pkgdesc = f"Linux kernel for Steam Deck {pkgver[0 : pkgver.rfind('.')]}.x"
license = "GPL-2.0-only"
url = "https://gitlab.com/evlaV/linux-integration"
source = f"{url}/-/archive/{pkgver}-valve{_vver}/linux-integration-{pkgver}-valve{_vver}.tar.gz"
sha256 = "3eec365f2b02f894b0fd802943a949f3d9caba4368bbbb4a91a58fa1614b15ca"
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
