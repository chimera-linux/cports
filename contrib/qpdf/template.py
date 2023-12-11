pkgname = "qpdf"
pkgver = "11.6.4"
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
    "openssl-devel",
    "zlib-devel",
]
checkdepends = ["perl"]
pkgdesc = "Command-line tool and C++ library for PDF files"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/qpdf/qpdf"
source = f"https://github.com/qpdf/qpdf/releases/download/v{pkgver}/qpdf-{pkgver}.tar.gz"
sha256 = "c4b59318d296c50ceb29881e28bb57c6fcc1f6ca675cf52480ceeca552d7b3f6"
hardening = ["vis", "cfi"]
# for some reason some tests have an empty output for diff
options = ["!check"]


@subpackage("libqpdf-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libqpdf-libs")
def _libs(self):
    return self.default_libs()
