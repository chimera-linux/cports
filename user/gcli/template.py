pkgname = "gcli"
pkgver = "2.13.0"
pkgrel = 0
build_style = "configure"
configure_args = ["--prefix=/usr"]
hostmakedepends = ["byacc", "flex", "kyua", "pkgconf"]
makedepends = [
    "atf-devel",
    "curl-devel",
    "libedit-devel",
    "lowdown-devel",
    "musl-bsd-headers",
    "openssl3-devel",
]
pkgdesc = "CLI tool for interacting with Git(Hub|Lab|Tea)"
license = "BSD-2-Clause"
url = "https://herrhotzenplotz.de/gcli"
source = f"{url}/releases/gcli-{pkgver}/gcli-{pkgver}.tar.xz"
sha256 = "b1fe3a67b447fcabf6f0dbe3216c86caf63de24df0640b4fa579bdeb5791acab"


def post_install(self):
    self.install_license("LICENSE")
