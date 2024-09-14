pkgname = "libppd"
pkgver = "2.0.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    # TODO mupdf deptree
    "--disable-mutool",
]
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "libtool",
    "pkgconf",
    "poppler",
]
makedepends = [
    "cups-devel",
    "libcupsfilters-devel",
    "linux-headers",
]
pkgdesc = "Legacy support library for PPD files"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0 AND custom:gpl-exception"
url = "https://github.com/OpenPrinting/libppd"
source = f"https://github.com/OpenPrinting/libppd/releases/download/{pkgver}/libppd-{pkgver}.tar.xz"
sha256 = "882d3c659a336e91559de8f3c76fc26197fe6e5539d9b484a596e29a5a4e0bc8"
# vis breaks symbols
hardening = ["!vis"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libppd-devel")
def _(self):
    return self.default_devel()
