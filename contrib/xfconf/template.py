pkgname = "xfconf"
pkgver = "4.18.2"
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
sha256 = "dce24fb0555e9718d139c10e714759e03ab4e40a7ffcf3c990f046f7a17213cc"


@subpackage("xfconf-devel")
def _dev(self):
    return self.default_devel()
