pkgname = "stagit"
pkgver = "1.3"
pkgrel = 0
build_style = "makefile"
make_build_args = [
    "COMPATOBJ=",
    "COMPATSRC=",
    "LIBGIT_INC=-I/usr/include",
    "LIBGIT_LIB=-lgit2",
]
make_install_args = ["MANPREFIX=/usr/share/man"]
makedepends = ["libgit2-devel"]
pkgdesc = "Static git page generator"
license = "ISC"
url = "https://codemadness.org/stagit.html"
source = f"https://codemadness.org/releases/stagit/stagit-{pkgver}.tar.gz"
sha256 = "a265be67d2c5639094643f16c81d817c626d7557ed7886c9310a1ba317237f8d"
hardening = ["vis", "cfi"]
# no tests defined
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
