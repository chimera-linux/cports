pkgname = "libxkbcommon"
pkgver = "1.6.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Denable-x11=true",
    "-Denable-wayland=true",
    "-Denable-xkbregistry=true",
    "-Denable-docs=false",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "bison",
    "wayland-protocols",
    "wayland-progs",
]
makedepends = [
    "xkeyboard-config",
    "libxcb-devel",
    "wayland-devel",
    "wayland-protocols",
    "xorgproto",
    "libxml2-devel",
]
depends = ["xkeyboard-config"]
pkgdesc = "Library to handle keyboard descriptions"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xkbcommon.org"
source = f"https://github.com/xkbcommon/libxkbcommon/archive/xkbcommon-{pkgver}.tar.gz"
sha256 = "4aa6c1cad7dce1238d6f48b6729f1998c7e3f0667a21100d5268c91a5830ad7b"


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
