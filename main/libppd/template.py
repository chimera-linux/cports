pkgname = "libppd"
pkgver = "2.1.0"
pkgrel = 2
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
source = f"{url}/releases/download/{pkgver}/libppd-{pkgver}.tar.xz"
sha256 = "bc4d7f8b749a8809f532459a5dd2f3513556ea2b96b3e12aced3e078c2697cba"
# vis breaks symbols
hardening = ["!vis"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libppd-devel")
def _(self):
    return self.default_devel()
