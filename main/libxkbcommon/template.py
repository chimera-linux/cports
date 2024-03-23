pkgname = "libxkbcommon"
pkgver = "1.7.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Denable-x11=true",
    "-Denable-wayland=true",
    "-Denable-xkbregistry=true",
    "-Denable-docs=false",
]
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
pkgdesc = "Library to handle keyboard descriptions"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xkbcommon.org"
source = f"https://github.com/xkbcommon/libxkbcommon/archive/xkbcommon-{pkgver}.tar.gz"
sha256 = "20d5e40dabd927f7a7f4342bebb1e8c7a59241283c978b800ae3bf60394eabc4"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libxkbcommon-x11")
def _x11(self):
    self.pkgdesc = f"{pkgdesc} (X11 support)"

    return ["usr/lib/*x11*.so.*"]


@subpackage("libxkbregistry")
def _registry(self):
    self.pkgdesc = "XKB API to query keyboard descriptions"

    return ["usr/lib/libxkbregistry.so.*"]


@subpackage("libxkbcommon-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libxkbcommon-progs")
def _progs(self):
    return self.default_progs(extra=["usr/libexec"])
