pkgname = "libxfce4util"
pkgver = "4.18.1"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake", "intltool", "vala"]
makedepends = ["glib-devel"]
pkgdesc = "Utility library for Xfce"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "https://xfce.org"
source = f"https://archive.xfce.org/src/xfce/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "8a52063a5adc66252238cad9ee6997909b59983ed21c77eb83c5e67829d1b01f"

@subpackage("libxfce4util-devel")
def _dev(self):
    return self.default_devel()

configure_gen = []
