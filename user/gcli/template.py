pkgname = "gcli"
pkgver = "2.11.0"
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
sha256 = "ffab851dd95defd6eb33b6b4603313272f3be439980033b1afcabe035022beb0"


def post_install(self):
    self.install_license("LICENSE")
