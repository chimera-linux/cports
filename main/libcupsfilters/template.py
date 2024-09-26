pkgname = "libcupsfilters"
pkgver = "2.0.0"
pkgrel = 2
build_style = "gnu_configure"
configure_args = [
    # TODO mupdf deptree
    "--disable-mutool",
    "--with-test-font-path=/usr/share/fonts/dejavu/DejaVuSans.otf",
]
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
checkdepends = ["fonts-dejavu-otf"]
depends = ["ghostscript"]
pkgdesc = "Support library for cups filters"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0 AND custom:gpl-exception"
url = "https://github.com/OpenPrinting/libcupsfilters"
source = f"https://github.com/OpenPrinting/libcupsfilters/releases/download/{pkgver}/libcupsfilters-{pkgver}.tar.xz"
sha256 = "542f2bfbc58136a4743c11dc8c86cee03c9aca705612654e36ac34aa0d9aa601"
# vis breaks symbols
hardening = ["!vis"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libcupsfilters-devel")
def _(self):
    return self.default_devel()
