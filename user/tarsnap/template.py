pkgname = "tarsnap"
pkgver = "1.0.40"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
makedepends = [
    "e2fsprogs-devel",
    "openssl3-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Online backups for the truly paranoid"
maintainer = "Nasado <hi@nasado.name>"
license = "custom:tarsnap"
url = "https://www.tarsnap.com"
source = f"{url}/download/tarsnap-autoconf-{pkgver}.tgz"
sha256 = "bccae5380c1c1d6be25dccfb7c2eaa8364ba3401aafaee61e3c5574203c27fd5"


def post_install(self):
    self.install_license("COPYING")
