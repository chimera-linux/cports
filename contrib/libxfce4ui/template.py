pkgname = "libxfce4ui"
pkgver = "4.18.6"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-tests", "--disable-static"]
make_cmd = "gmake"
# TODO: gobject-introspection, fails to build with it for some reason
hostmakedepends = [
    "automake",
    "gettext-devel",
    "glib-devel",
    "gmake",
    "gtk-doc-tools",
    "intltool",
    "libtool",
    "pkgconf",
    "python",
    "vala-devel",
    "xfce4-dev-tools",
]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
    "libgtop-devel",
    "libsm-devel",
    "libxfce4util-devel",
    "libxml2-devel",
    "startup-notification-devel",
    "vala-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce UI library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "https://docs.xfce.org/xfce/libxfce4ui/start"
source = (
    f"$(XFCE_SITE)/xfce/libxfce4ui/{pkgver[:-2]}/libxfce4ui-{pkgver}.tar.bz2"
)
sha256 = "77dd99206cc8c6c7f69c269c83c7ee6a037bca9d4a89b1a6d9765e5a09ce30cd"


@subpackage("libxfce4ui-devel")
def _dev(self):
    return self.default_devel()
