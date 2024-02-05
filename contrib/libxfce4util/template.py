pkgname = "libxfce4util"
pkgver = "4.18.2"
pkgrel = 0
build_style = "gnu_configure"
# generates invalid configure
configure_gen = []
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake", "intltool", "vala"]
makedepends = ["glib-devel"]
pkgdesc = "Utility library for Xfce"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "https://xfce.org"
source = f"https://archive.xfce.org/src/xfce/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "d9a329182b78f7e2520cd4aafcbb276bbbf162f6a89191676539ad2e3889c353"


@subpackage("libxfce4util-devel")
def _dev(self):
    return self.default_devel()
