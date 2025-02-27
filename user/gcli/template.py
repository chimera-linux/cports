pkgname = "gcli"
pkgver = "2.6.1"
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
sha256 = "ce91365eb6220056a1326cfa2afe287b7bb1708de9af12141dab21a00965c79a"


def post_install(self):
    self.install_license("LICENSE")
