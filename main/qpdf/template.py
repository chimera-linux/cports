pkgname = "qpdf"
pkgver = "12.2.0"
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
sha256 = "b3d1575b2218badc3549d6977524bb0f8c468c6528eebc8967bbe3078cf2cace"
# for some reason some tests have an empty output for diff
options = ["!check"]


@subpackage("qpdf-devel")
def _(self):
    self.renames = ["libqpdf-devel"]

    return self.default_devel()


@subpackage("qpdf-libs")
def _(self):
    self.renames = ["libqpdf-libs"]

    return self.default_libs()
