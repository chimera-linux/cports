pkgname = "rauc"
pkgver = "1.14"
pkgrel = 2
build_style = "meson"
configure_args = ["-Dstreaming=false"]
hostmakedepends = [
    "glib-devel",
    "meson",
    "pkgconf",
]
makedepends = [
    "curl-devel",
    "dbus-devel",
    "glib-devel",
    "json-glib-devel",
    "linux-headers",
    "openssl3-devel",
    "util-linux-fdisk-devel",
]
depends = [
    "squashfs-tools",
]
pkgdesc = "Safe and secure software updates for embedded Linux"
license = "LGPL-2.1-only"
url = "https://rauc.io"
source = f"https://github.com/rauc/rauc/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c6a59179378d44fcf648e2da0beccf8d7fc06708f6face4f799b655830fe8889"
# check: depends on network
options = ["!check"]


def post_install(self):
    self.uninstall("usr/lib/systemd")
    self.uninstall("usr/share/rauc/rauc.service")
    self.install_license("COPYING")
