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
source = f"https://download.tuxfamily.org/ctpl/releases/ctpl-{pkgver}.tar.gz"
sha256 = "21108fc7567ed216deea4591adbfece8e88b1f4bb1ca77c37400920644d756be"


@subpackage("ctpl-devel")
def _(self):
    return self.default_devel()
