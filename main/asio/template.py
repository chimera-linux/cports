pkgname = "asio"
pkgver = "1.38.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf"]
makedepends = [
    "boost-devel",
    "openssl3-devel",
]
pkgdesc = "Asynchronous I/O library for C++"
license = "BSL-1.0"
url = "https://think-async.com/Asio"
source = f"$(SOURCEFORGE_SITE)/asio/asio-{pkgver}.tar.bz2"
sha256 = "c04e0e66ac29741faad763a56f3c50196421d4b968009fc237c53314769bf8ad"


def post_install(self):
    self.install_license("LICENSE_1_0.txt")
