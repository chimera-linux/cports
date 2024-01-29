pkgname = "bemenu"
pkgver = "0.6.17"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["scdoc", "gmake", "pkgconf"]
makedepends = [
    "cairo-devel",
    "libx11-devel",
    "libxinerama-devel",
    "libxkbcommon-devel",
    "linux-headers",
    "ncurses-devel",
    "pango-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Dynamic menu library and client program inspired by dmenu"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "GPL-3.0-only AND LGPL-3.0-only"
url = "https://github.com/Cloudef/bemenu"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "74480e7874fd75f0af38d86132043c0a82d0b1355827e8ad4f511e72f438dbf8"
hardening = ["vis", "!cfi"]
# no check target defined
options = ["!check"]


@subpackage(f"{pkgname}-devel")
def _devel(self):
    return self.default_devel()


@subpackage(f"{pkgname}-curses")
def _curses(self):
    self.pkgdesc = f"{pkgdesc} (curses backend)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "ncurses"]

    return ["usr/lib/bemenu/bemenu-renderer-curses.so"]


@subpackage(f"{pkgname}-wayland")
def _wayland(self):
    self.pkgdesc = f"{pkgdesc} (wayland backend)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "wayland"]

    return ["usr/lib/bemenu/bemenu-renderer-wayland.so"]


@subpackage(f"{pkgname}-x11")
def _x11(self):
    self.pkgdesc = f"{pkgdesc} (x11 backend)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "libx11"]

    return ["usr/lib/bemenu/bemenu-renderer-x11.so"]
