pkgname = "gcli"
pkgver = "2.8.0"
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
sha256 = "b3ee6eb0d694f47f15a6d6e4f5adc824059e3f6836dfe95e74bd3a0cf92f05ec"


def post_install(self):
    self.install_license("LICENSE")
