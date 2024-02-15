pkgname = "libtracefs"
pkgver = "1.8.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    # same as libtraceevent, useless static plugins
    "-Ddefault_library=shared",
    "-Dasciidoctor=false",
]
hostmakedepends = [
    "asciidoc",
    "bison",
    "flex",
    "gsed",
    "meson",
    "pkgconf",
    "xmlto",
]
makedepends = [
    "cunit-devel",
    "libtraceevent-devel",
    "linux-headers",
]
pkgdesc = "Linux kernel trace file system library"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-or-later"
url = "https://git.kernel.org/pub/scm/libs/libtrace/libtracefs.git/about"
source = f"https://git.kernel.org/pub/scm/libs/libtrace/libtracefs.git/snapshot/libtracefs-{pkgver}.tar.gz"
sha256 = "f92475d5c4cb509983697fb359ee615bef4f08ed8bdc9c690f6118ba68886de0"
# vis breaks symbols
hardening = ["!vis"]


@subpackage("libtracefs-devel")
def _devel(self):
    return self.default_devel()
