pkgname = "libcupsfilters"
pkgver = "2.1.0"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    # TODO mupdf deptree
    "--disable-mutool",
    "--with-test-font-path=/usr/share/fonts/dejavu/DejaVuSans.otf",
]
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "ghostscript",
    "libtool",
    "pkgconf",
]
makedepends = [
    "cups-devel",
    "fontconfig-devel",
    "lcms2-devel",
    "libexif-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libqpdf-devel",
    "libtiff-devel",
    "linux-headers",
    "poppler-devel",
]
checkdepends = ["bash", "fonts-dejavu-otf"]
depends = ["ghostscript"]
pkgdesc = "Support library for cups filters"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0 AND custom:gpl-exception"
url = "https://github.com/OpenPrinting/libcupsfilters"
source = f"{url}/releases/download/{pkgver}/libcupsfilters-{pkgver}.tar.xz"
sha256 = "cbe900c7783e4aab0b1681629fad7322d82d082a51e8bae7e1c741d26bdcd294"
# vis breaks symbols
hardening = ["!vis"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libcupsfilters-devel")
def _(self):
    return self.default_devel()
