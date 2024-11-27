pkgname = "gmime"
pkgver = "3.2.15"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-gtk-doc",
    "--disable-static",
]
# default build/ dir exists and so builds from wrong dir
make_dir = "."
hostmakedepends = [
    "automake",
    "gtk-doc-tools",
    "libtool",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "gpgme-devel",
    "libidn2-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "C/C++ MIME creation and parser library"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/jstedfast/gmime"
source = f"{url}/releases/download/{pkgver}/gmime-{pkgver}.tar.xz"
sha256 = "84cd2a481a27970ec39b5c95f72db026722904a2ccf3fdbd57b280cf2d02b5c4"
# vis breaks symbols
hardening = []


@subpackage("gmime-devel")
def _(self):
    return self.default_devel()
