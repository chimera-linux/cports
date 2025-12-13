pkgname = "xfce4-panel"
pkgver = "4.20.5"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "glib-devel",
    "gobject-introspection",
    "gtk-doc-tools",
    "pkgconf",
    "slibtool",
    "xfce4-dev-tools",
]
makedepends = [
    "cairo-devel",
    "exo-devel",
    "garcon-devel",
    "glib-devel",
    "gtk+3-devel",
    "gtk-layer-shell-devel",
    "libdbusmenu-devel",
    "libwnck-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "libxfce4windowing-devel",
    "libyaml-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce panel"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://docs.xfce.org/xfce/xfce4-panel/start"
source = (
    f"$(XFCE_SITE)/xfce/xfce4-panel/{pkgver[:-2]}/xfce4-panel-{pkgver}.tar.bz2"
)
sha256 = "3f91850c9c467680c8081d561f1a3fd83355c07db07be9a96da1764f8c842b2b"
# introspection
options = ["!cross"]


@subpackage("xfce4-panel-devel")
def _(self):
    return self.default_devel()
