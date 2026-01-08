pkgname = "libxkbcommon"
pkgver = "1.13.1"
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
sha256 = "aeb951964c2f7ecc08174cb5517962d157595e9e3f38fc4a130b91dc2f9fec18"


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
