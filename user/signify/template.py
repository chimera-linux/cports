pkgname = "signify"
pkgver = "32"
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
url = "https://github.com/aperezdc/signify"
source = f"https://github.com/aperezdc/signify/releases/download/v{pkgver}/signify-{pkgver}.tar.xz"
sha256 = "6dd1b97fd9273d268b70c1be3c2592cbbe1488bca5e45c12c58f8c74362758d5"


def post_install(self):
    self.install_license("COPYING")
