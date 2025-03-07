pkgname = "gcli"
pkgver = "2.7.0"
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
sha256 = "0959780bb0eb96548c32b9f908baa5dcad5fa070c8572769972ea9381a27ddf5"


def post_install(self):
    self.install_license("LICENSE")
