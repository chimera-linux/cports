pkgname = "sfeed"
pkgver = "2.2"
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
sha256 = "4270389c3cfa474caa3892271c3171a751490328cc52e502d8435de3c2e41cc5"
hardening = ["vis", "cfi"]
# no tests defined
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
