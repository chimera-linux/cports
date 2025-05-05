pkgname = "libtracefs"
pkgver = "1.8.2"
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
license = "LGPL-2.1-or-later"
url = "https://git.kernel.org/pub/scm/libs/libtrace/libtracefs.git/about"
source = f"https://git.kernel.org/pub/scm/libs/libtrace/libtracefs.git/snapshot/libtracefs-{pkgver}.tar.gz"
sha256 = "255980e1da5648fbbc32777ed8457b485b2b96f3449674610b46d9c437271209"
# vis breaks symbols
hardening = ["!vis"]
# bashcomp name does not match
options = ["!lintcomp"]


@subpackage("libtracefs-devel")
def _(self):
    return self.default_devel()
