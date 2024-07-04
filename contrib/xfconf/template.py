pkgname = "xfconf"
pkgver = "4.18.3"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--enable-gsettings-backend"]
make_cmd = "gmake"
make_dir = "."
make_check_wrapper = [
    "dbus-run-session",
    "--",
    "xwfb-run",
    "--",
]
hostmakedepends = [
    "automake",
    "glib-devel",
    "gmake",
    "gobject-introspection",
    "gtk-doc-tools",
    "intltool",
    "libtool",
    "pkgconf",
    "python",
    "vala-devel",
    "xfce4-dev-tools",
]
makedepends = ["glib-devel", "libxfce4util-devel", "vala-devel"]
checkdepends = ["dbus", "xwayland-run"]
pkgdesc = "Xfce configuration system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND LGPL-2.0-or-later"
url = "https://docs.xfce.org/xfce/xfconf/start"
source = f"$(XFCE_SITE)/xfce/xfconf/{pkgver[:-2]}/xfconf-{pkgver}.tar.bz2"
sha256 = "c56cc69056f6947b2c60b165ec1e4c2b0acf26a778da5f86c89ffce24d5ebd98"
options = ["!cross"]


@subpackage("xfconf-devel")
def _devel(self):
    return self.default_devel()
