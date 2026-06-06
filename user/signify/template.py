pkgname = "signify"
pkgver = "33"
pkgrel = 0
build_style = "makefile"
make_install_args = [
    f"DESTDIR=/destdir/{pkgname}-{pkgver}/{pkgname}",
    "PREFIX=/usr",
]
hostmakedepends = ["pkgconf"]
makedepends = ["libbsd-devel"]
pkgdesc = "OpenBSD tool to sign and verify signatures on files"
license = "ISC"
url = "https://codeberg.org/aperezdc/signify"
source = f"https://codeberg.org/aperezdc/signify/releases/download/v{pkgver}/signify-{pkgver}.tar.xz"
sha256 = "61635e45abcf1c78e28fbe3534a4224a2251c39295bb70bb211f699ef5f6eb27"


def post_install(self):
    self.install_license("COPYING")
