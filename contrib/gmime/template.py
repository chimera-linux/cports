pkgname = "gmime"
pkgver = "3.2.14"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-gtk-doc",
    "--disable-static",
]
make_cmd = "gmake"
# default build/ dir exists and so builds from wrong dir
make_dir = "."
hostmakedepends = [
    "autoconf",
    "automake",
    "gmake",
    "gtk-doc-tools",
    "libtool",
    "pkgconf",
]
makedepends = [
    "libidn2-devel",
    "glib-devel",
    "gpgme-devel",
    "zlib-devel",
]
pkgdesc = "C/C++ MIME creation and parser library"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-or-later"
url = "https://github.com/jstedfast/gmime"
source = f"{url}/releases/download/{pkgver}/gmime-{pkgver}.tar.xz"
sha256 = "a5eb3dd675f72e545c8bc1cd12107e4aad2eaec1905eb7b4013cdb1fbe5e2317"
# vis breaks symbols
hardening = []


@subpackage("gmime-devel")
def _devel(self):
    return self.default_devel()
