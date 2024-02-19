pkgname = "sfeed"
pkgver = "2.0"
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
sha256 = "8e6a7e6e1d7e86034ae27035e37a8f7fc98bc25fe35120bd18ff07e04f18e91d"
hardening = ["vis", "cfi"]
# no tests defined
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
