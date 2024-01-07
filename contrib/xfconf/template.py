pkgname = "xfconf"
pkgver = "4.18.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-gsettings-backend"]
# broken presently
configure_gen = []
make_cmd = "gmake"
make_check_wrapper = ["dbus-run-session", "xvfb-run"]
hostmakedepends = [
    "glib-devel",
    "gmake",
    "intltool",
    "pkgconf",
    "python",
    "vala-devel",
]
makedepends = ["glib-devel", "vala-devel", "libxfce4util-devel"]
checkdepends = ["xserver-xorg-xvfb", "dbus"]
pkgdesc = "Xfce configuration system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND LGPL-2.0-or-later"
url = "https://xfce.org"
source = f"https://archive.xfce.org/src/xfce/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "c56cc69056f6947b2c60b165ec1e4c2b0acf26a778da5f86c89ffce24d5ebd98"


@subpackage("xfconf-devel")
def _dev(self):
    return self.default_devel()
