pkgname = "sfeed"
pkgver = "2.1"
pkgrel = 0
build_style = "makefile"
make_install_args = [
    "COMPATOBJ=",
    "COMPATSRC=",
    "PREFIX=/usr",
    "MANPREFIX=/usr/share/man",
]
makedepends = ["ncurses-devel"]
pkgdesc = "RSS and Atom feed fetcher"
maintainer = "ttyyls <contact@behri.org>"
license = "ISC"
url = "https://codemadness.org/sfeed.html"
source = f"https://codemadness.org/releases/sfeed/sfeed-{pkgver}.tar.gz"
sha256 = "dd54c9b3ff8c47a67ceae64b8cd62b064ebbf2f11715386d89603ecd276e3705"
hardening = ["vis", "cfi"]
# no tests defined
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
