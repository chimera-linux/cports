pkgname = "stagit"
pkgver = "1.2"
pkgrel = 2
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
maintainer = "ttyyls <contact@behri.org>"
license = "ISC"
url = "https://codemadness.org/stagit.html"
source = f"https://codemadness.org/releases/stagit/stagit-{pkgver}.tar.gz"
sha256 = "5659bd8ba7e1417edd40f7b7781a8ea26939ab6aa513409023835f04875921c5"
hardening = ["vis", "cfi"]
# no tests defined
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
