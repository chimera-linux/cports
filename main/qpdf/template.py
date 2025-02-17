pkgname = "qpdf"
pkgver = "11.10.1"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/qpdf/qpdf"
source = f"{url}/releases/download/v{pkgver}/qpdf-{pkgver}.tar.gz"
sha256 = "defca435cf57d26f8a0619864841aa21f5469fddc6eb5662f62d8443021c069d"
# for some reason some tests have an empty output for diff
options = ["!check"]


@subpackage("qpdf-devel")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libqpdf-devel")]

    return self.default_devel()


@subpackage("qpdf-libs")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libqpdf-libs")]

    return self.default_libs()
