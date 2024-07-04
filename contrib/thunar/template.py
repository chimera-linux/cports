pkgname = "thunar"
pkgver = "4.18.10"
pkgrel = 1
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gmake",
    "gobject-introspection",
    "gtk-doc-tools",
    "intltool",
    "libtool",
    "pkgconf",
    "xfce4-dev-tools",
]
makedepends = [
    "exo-devel",
    "gdk-pixbuf-devel",
    "glib-devel",
    "gtk+3-devel",
    "libgudev-devel",
    "libnotify-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "pango-devel",
    "xfce4-panel-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce file manager"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://docs.xfce.org/xfce/thunar/start"
source = f"$(XFCE_SITE)/xfce/thunar/{'.'.join(pkgver.split('.')[:-1])}/thunar-{pkgver}.tar.bz2"
sha256 = "e8308a1f139602d8c125f594bfcebb063b7dac1fbb6e14293bab4cdb3ecf1d08"
options = ["!cross"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")


@subpackage("thunar-devel")
def _devel(self):
    return self.default_devel()
