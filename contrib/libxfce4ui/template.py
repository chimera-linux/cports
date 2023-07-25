pkgname = "libxfce4ui"
pkgver = "4.18.4"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--enable-tests", "--disable-static"]
configure_gen = []
make_cmd = "gmake"
hostmakedepends = [
    "pkgconf",
    "gmake",
    "intltool",
    "vala-devel",
    "glib-devel",
    "gettext-tiny-devel",
    "python",
]
makedepends = [
    "glib-devel",
    "vala-devel",
    "gtk+3-devel",
    "libxfce4util-devel",
    "xfconf-devel",
    "libxml2-devel",
    "startup-notification-devel",
    "libsm-devel",
    "libgtop-devel",
]
pkgdesc = "Xfce UI library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "https://xfce.org"
source = f"https://archive.xfce.org/src/xfce/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "87eefe797c6d26de3f754de48872faf131f1b5fc93fb88e22f5c7886a842cb4c"


@subpackage("libxfce4ui-devel")
def _dev(self):
    return self.default_devel()
