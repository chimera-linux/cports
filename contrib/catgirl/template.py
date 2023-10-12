pkgname = "catgirl"
pkgver = "2.2"
pkgrel = 1
build_style = "configure"
configure_args = ["--prefix=/usr", "--mandir=/usr/share/man"]
make_build_target = "all"
hostmakedepends = [
    "pkgconf",
]
makedepends = [
    "libretls-devel",
    "ncurses-devel",
]
pkgdesc = "Terminal IRC client"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://git.causal.agency/catgirl"
source = f"{url}/snapshot/{pkgname}-{pkgver}.tar.gz"
sha256 = "fb6d04a099303af05d278c705c1542e7ee61643c030d6a0b68dec5371080a3c7"
# FIXME: cfi
hardening = ["vis"]
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
