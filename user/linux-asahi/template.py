# make sure to also change update.py
pkgname = "linux-asahi"
pkgver = "6.14.1"
pkgrel = 0
_asahiver = 2
archs = ["aarch64"]
build_style = "linux-kernel"
configure_args = ["FLAVOR=asahi", f"RELEASE={pkgrel}"]
make_dir = "build"
hostmakedepends = ["base-kernel-devel", "rust", "rust-bindgen"]
makedepends = ["rust-src"]
depends = ["base-kernel"]
provides = ["linux"]
pkgdesc = f"Asahi Linux kernel {pkgver[0 : pkgver.rfind('.')]}.x"
license = "GPL-2.0-only"
url = "https://asahilinux.org"
source = f"https://github.com/AsahiLinux/linux/archive/refs/tags/asahi-{pkgver}-{_asahiver}.tar.gz"
sha256 = "5198af2e2504462ebfc6867f4956909d8714e57fd3ae0d64948ed0355dd00c8f"
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


@subpackage("linux-asahi-devel")
def _(self):
    self.depends += ["clang"]
    self.options = ["foreignelf", "execstack", "!scanshlibs"]
    return ["usr/src", "usr/lib/modules/*/build"]


@subpackage("linux-asahi-dbg", self.build_dbg)
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
