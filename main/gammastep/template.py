pkgname = "gammastep"
pkgver = "2.0.10"
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
    "libxcb-devel",
    "libxxf86vm-devel",
    "libx11-devel",
    "wayland-devel",
]
depends = ["gtk+3", "libayatana-appindicator", "python-gobject", "python-pyxdg"]
pkgdesc = "Adjusts the color temperature of the screen"
license = "GPL-3.0-or-later"
url = "https://gitlab.com/chinstrap/gammastep"
source = f"{url}/-/archive/v{pkgver}/gammastep-v{pkgver}.tar.gz"
sha256 = "f00549fa856ebdcdbbbcd2bcb35cc3e355e6f19284d9e8fb6cadff9bee17c325"


def post_install(self):
    self.install_file(
        "gammastep.conf.sample",
        "usr/share/examples/gammastep",
        name="config.ini.example",
    )
    self.install_service(self.files_path / "gammastep.user")
