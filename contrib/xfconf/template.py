pkgname = "xfconf"
pkgver = "4.18.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-gsettings-backend"]
make_cmd = "gmake"
make_check_wrapper = ["dbus-run-session", "xvfb-run"]
hostmakedepends = [
    "pkgconf", "gmake", "intltool", "vala-devel", "glib-devel", "python"
]
makedepends = ["glib-devel", "vala-devel", "libxfce4util-devel"]
checkdepends = ["xserver-xorg-xvfb", "dbus"]
pkgdesc = "Xfce configuration system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND LGPL-2.0-or-later"
url = "https://xfce.org"
source = f"https://archive.xfce.org/src/xfce/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "d9714751bbcfdc5a59340da6ef8ddfc0807221587b962d907f97dc0a8a002257"

@subpackage("xfconf-devel")
def _dev(self):
    return self.default_devel()
