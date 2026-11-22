pkgname = "qpdf"
pkgver = "12.4.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_DOC_PDF=OFF",
    "-DINSTALL_EXAMPLES=OFF",
]
make_check_env = {"LANG": "C"}
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "libjpeg-turbo-devel",
    "openssl3-devel",
    "zlib-ng-compat-devel",
]
checkdepends = ["perl"]
pkgdesc = "Command-line tool and C++ library for PDF files"
license = "Apache-2.0"
url = "https://github.com/qpdf/qpdf"
source = f"{url}/releases/download/v{pkgver}/qpdf-{pkgver}.tar.gz"
sha256 = "8a58af5b6141319287c1883bec8bd1bd545b7567b7fc5e6ce5d25a1c85f36397"


@subpackage("qpdf-devel")
def _(self):
    self.renames = ["libqpdf-devel"]

    return self.default_devel()


@subpackage("qpdf-libs")
def _(self):
    self.renames = ["libqpdf-libs"]

    return self.default_libs()
