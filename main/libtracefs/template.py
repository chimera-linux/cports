pkgname = "libtracefs"
pkgver = "1.8.1"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://git.kernel.org/pub/scm/libs/libtrace/libtracefs.git/about"
source = f"https://git.kernel.org/pub/scm/libs/libtrace/libtracefs.git/snapshot/libtracefs-{pkgver}.tar.gz"
sha256 = "d295aa20d711c313a9e229dbd15ba14026f0c1a50d57ae8b0823cc561b23745f"
# vis breaks symbols
hardening = ["!vis"]


@subpackage("libtracefs-devel")
def _(self):
    return self.default_devel()
