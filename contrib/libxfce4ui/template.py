pkgname = "libxfce4ui"
pkgver = "4.18.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-tests", "--disable-static"]
make_cmd = "gmake"
hostmakedepends = [
    "pkgconf", "gmake", "intltool", "vala-devel", "glib-devel",
    "gettext-tiny-devel", "python"
]
makedepends = [
    "glib-devel", "vala-devel", "gtk+3-devel", "glade3-devel",
    "libxfce4util-devel", "xfconf-devel", "libxml2-devel",
    "startup-notification-devel", "libsm-devel", "libgtop-devel",
]
pkgdesc = "Xfce UI library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "https://xfce.org"
source = f"https://archive.xfce.org/src/xfce/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "afa3a46eeed3ab612d2f7e1308edaf5819f6c33ccc16c13080efabd58f010abd"

@subpackage("libxfce4ui-devel")
def _dev(self):
    return self.default_devel()
