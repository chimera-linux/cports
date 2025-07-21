pkgname = "gammastep"
pkgver = "2.0.11"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext-devel",
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
    "libx11-devel",
    "libxcb-devel",
    "libxxf86vm-devel",
    "wayland-devel",
]
depends = ["gtk+3", "libayatana-appindicator", "python-gobject", "python-pyxdg"]
pkgdesc = "Adjusts the color temperature of the screen"
license = "GPL-3.0-or-later"
url = "https://gitlab.com/chinstrap/gammastep"
source = f"{url}/-/archive/v{pkgver}/gammastep-v{pkgver}.tar.gz"
sha256 = "e16026b8f21d5e02cfe7cd2f738c80f150c1f06a098e5e47e0fc088244a763bd"


def post_install(self):
    self.install_file(
        "gammastep.conf.sample",
        "usr/share/examples/gammastep",
        name="config.ini.example",
    )
    self.install_service(self.files_path / "gammastep.user")
