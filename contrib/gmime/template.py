pkgname = "gmime"
pkgver = "3.2.13"
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
sha256 = "2e10a54d4821daf8b16c019ad5d567e0fb8e766f8ffe5fec3d4c6a37373d6406"
# vis breaks symbols
hardening = []


@subpackage("gmime-devel")
def _devel(self):
    return self.default_devel()
