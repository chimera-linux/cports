pkgname = "libxkbcommon"
pkgver = "1.10.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX libexecdir
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
renames = ["libxkbregistry"]
pkgdesc = "Library to handle keyboard descriptions"
license = "MIT"
url = "https://xkbcommon.org"
source = f"https://github.com/xkbcommon/libxkbcommon/archive/xkbcommon-{pkgver}.tar.gz"
sha256 = "0427585a4d6ca17c9fc1ac4b539bf303348e9080af70c5ea402503bc370a9631"


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
