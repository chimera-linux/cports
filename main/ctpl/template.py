pkgname = "ctpl"
pkgver = "0.3.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static"]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gtk-doc-tools",
    "libtool",
    "pkgconf",
]
makedepends = [
    "glib-devel",
]
pkgdesc = "C template library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://ctpl.tuxfamily.org"
source = f"https://github.com/b4n/ctpl/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ae60c79316c6dc3a2935d906b8a911ce4188e8638b6e9b65fc6c04a5ca6bcdda"


@subpackage("ctpl-devel")
def _(self):
    return self.default_devel()
