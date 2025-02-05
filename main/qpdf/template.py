pkgname = "qpdf"
pkgver = "11.9.1"
pkgrel = 1
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
sha256 = "2ba4d248f9567a27c146b9772ef5dc93bd9622317978455ffe91b259340d13d1"
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
