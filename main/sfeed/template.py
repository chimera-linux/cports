pkgname = "sfeed"
pkgver = "2.4"
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
license = "ISC"
url = "https://codemadness.org/sfeed.html"
source = f"https://codemadness.org/releases/sfeed/sfeed-{pkgver}.tar.gz"
sha256 = "f9503fe9205a8136f76a9b753c6007abad33e2a516807e416a986723db06e879"
hardening = ["vis", "cfi"]
# no tests defined
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
