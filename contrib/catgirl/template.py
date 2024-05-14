pkgname = "catgirl"
pkgver = "2.2a"
pkgrel = 0
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
sha256 = "c6d760aaee134e052586def7a9103543f7281fde6531fbcb41086470794297c2"
# FIXME: cfi
hardening = ["vis"]
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
