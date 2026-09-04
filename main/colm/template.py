pkgname = "colm"
pkgver = "0.14.7"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = ["automake", "libtool", "asciidoc"]
checkdepends = ["bash"]
pkgdesc = "COmputer Language Manipulation programming language"
license = "MIT"
url = "https://www.colm.net/open-source/colm"
source = f"https://www.colm.net/files/colm/colm-{pkgver}.tar.gz"
sha256 = "6037b31c358dda6f580f7321f97a182144a8401c690b458fcae055c65501977d"


def post_extract(self):
    self.mkdir("src/include")
    self.ln_s("..", "src/include/colm")


def check(self):
    self.do("./runtests", wrksrc="test")


def post_install(self):
    self.install_license("COPYING")


@subpackage("colm-devel")
def _(self):
    return self.default_devel()
