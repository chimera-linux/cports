pkgname = "gammastep"
pkgver = "2.0.9"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gmake",
    "intltool",
    "pkgconf",
    "python",
    "slibtool",
    "wayland-progs",
]
makedepends = [
    "geoclue-devel",
    "glib-devel",
    "libdrm-devel",
    "libxcb-devel",
    "libxxf86vm-devel",
    "libx11-devel",
    "wayland-devel",
]
depends = ["gtk+3", "libayatana-appindicator", "python-gobject", "python-pyxdg"]
pkgdesc = "Adjusts the color temperature of the screen"
maintainer = "jabuxas <lucasbarbieri.c@gmail.com>"
license = "GPL-3.0-or-later"
url = "https://gitlab.com/chinstrap/gammastep"
source = f"{url}/-/archive/v{pkgver}/gammastep-v{pkgver}.tar.gz"
sha256 = "bbb9d90e1cf30920c1017db4ce5c4652e4c7843fd4c4e34164d99ecbc3bbb4c0"


def post_install(self):
    self.install_file(
        "gammastep.conf.sample",
        "usr/share/examples/gammastep",
        name="config.ini.example",
    )
