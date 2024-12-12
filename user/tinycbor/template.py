pkgname = "tinycbor"
pkgver = "0.6.0"
pkgrel = 0
build_style = "makefile"
make_install_args = ["prefix=/usr"]
make_check_args = ["QMAKE=qmake6"]
hostmakedepends = [
    "file",
    "pkgconf",
]
checkdepends = ["qt6-qtbase-devel"]
pkgdesc = "Concise binary object representation library"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "MIT"
url = "https://github.com/intel/tinycbor"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "512e2c9fce74f60ef9ed3af59161e905f9e19f30a52e433fc55f39f4c70d27e4"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("tinycbor-devel")
def _(self):
    return self.default_devel()


@subpackage("tinycbor-progs")
def _(self):
    return self.default_progs()
