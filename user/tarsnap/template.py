pkgname = "tarsnap"
pkgver = "1.0.41"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
makedepends = [
    "e2fsprogs-devel",
    "openssl3-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Online backups for the truly paranoid"
license = "custom:tarsnap"
url = "https://www.tarsnap.com"
source = f"{url}/download/tarsnap-autoconf-{pkgver}.tgz"
sha256 = "bebdbe1e6e91233755beb42ef0b4adbefd9573455258f009fb331556c799b3d0"


def post_install(self):
    self.install_license("COPYING")
