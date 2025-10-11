pkgname = "libxfce4ui"
pkgver = "4.20.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-tests",
    "--disable-static",
    "--with-vendor-info=Chimera Linux",
]
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "glib-devel",
    "gobject-introspection",
    "gtk-doc-tools",
    "pkgconf",
    "python",
    "slibtool",
    "vala-devel",
    "xfce4-dev-tools",
]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
    "libepoxy-devel",
    "libgtop-devel",
    "libgudev-devel",
    "libsm-devel",
    "libxfce4util-devel",
    "libxml2-devel",
    "startup-notification-devel",
    "vala-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce UI library"
license = "LGPL-2.0-or-later"
url = "https://docs.xfce.org/xfce/libxfce4ui/start"
source = (
    f"$(XFCE_SITE)/xfce/libxfce4ui/{pkgver[:-2]}/libxfce4ui-{pkgver}.tar.bz2"
)
sha256 = "5d3d67b1244a10cee0e89b045766c05fe1035f7938f0410ac6a3d8222b5df907"
# introspection
options = ["!cross"]


@subpackage("libxfce4ui-devel")
def _(self):
    return self.default_devel()
