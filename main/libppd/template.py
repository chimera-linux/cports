pkgname = "libppd"
pkgver = "2.1.1"
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
license = "Apache-2.0 AND custom:gpl-exception"
url = "https://github.com/OpenPrinting/libppd"
source = f"{url}/releases/download/{pkgver}/libppd-{pkgver}.tar.xz"
sha256 = "3fa341cc03964046d2bf6b161d80c1b4b2e20609f38d860bcaa11cb70c1285e4"
# vis breaks symbols
hardening = ["!vis"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libppd-devel")
def _(self):
    return self.default_devel()
