pkgname = "libcupsfilters"
pkgver = "2.1.1"
pkgrel = 2
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
    "libtiff-devel",
    "linux-headers",
    "poppler-devel",
    "qpdf-devel",
]
checkdepends = ["bash", "fonts-dejavu-otf"]
depends = ["ghostscript"]
pkgdesc = "Support library for cups filters"
license = "Apache-2.0 AND custom:gpl-exception"
url = "https://github.com/OpenPrinting/libcupsfilters"
source = f"{url}/releases/download/{pkgver}/libcupsfilters-{pkgver}.tar.xz"
sha256 = "6c303e36cfde05a6c88fb940c62b6a18e7cdbfb91f077733ebc98f104925ce36"
# vis breaks symbols
hardening = ["!vis"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libcupsfilters-devel")
def _(self):
    return self.default_devel()
