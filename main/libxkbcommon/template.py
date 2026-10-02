pkgname = "libxkbcommon"
pkgver = "1.13.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Denable-x11=true",
    "-Denable-wayland=true",
    "-Denable-xkbregistry=true",
    "-Denable-docs=false",
]
# pulling in xserver-xorg-xvfb creates a cycle
make_check_args = ["--no-suite", "x11"]
hostmakedepends = [
    "bison",
    "meson",
    "pkgconf",
    "wayland-progs",
    "wayland-protocols",
]
makedepends = [
    "libxcb-devel",
    "libxml2-devel",
    "wayland-devel",
    "wayland-protocols",
    "xkeyboard-config",
    "xorgproto",
]
depends = ["xkeyboard-config"]
renames = ["libxkbregistry"]
pkgdesc = "Library to handle keyboard descriptions"
license = "MIT"
url = "https://xkbcommon.org"
source = f"https://github.com/xkbcommon/libxkbcommon/archive/xkbcommon-{pkgver}.tar.gz"
sha256 = "acc4d5f7c3cbba5f9f8d08d8bdbeede84ecede46792f47929aa9321873385528"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libxkbcommon-x11")
def _(self):
    self.subdesc = "X11 support"

    return ["usr/lib/*x11*.so.*"]


@subpackage("libxkbcommon-devel")
def _(self):
    return self.default_devel()


@subpackage("libxkbcommon-progs")
def _(self):
    return self.default_progs(extra=["usr/lib/xkbcommon"])
