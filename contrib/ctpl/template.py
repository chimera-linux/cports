pkgname = "ctpl"
pkgver = "0.3.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static"]
configure_gen = ["./autogen.sh"]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gtk-doc-tools",
    "libtool",
    "pkgconf"
]
makedepends = [
    "glib-devel",
]
pkgdesc = "C template library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://ctpl.tuxfamily.org"
source = f"https://download.tuxfamily.org/ctpl/releases/ctpl-{pkgver}.tar.gz"
sha256 = "3a95fdd03437ed3ae222339cb0de2d2c1240d627faa6c77bf46f1a9b761729fb"


@subpackage("ctpl-devel")
def _devel(self):
    return self.default_devel()
