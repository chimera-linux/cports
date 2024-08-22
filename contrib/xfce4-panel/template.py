pkgname = "xfce4-panel"
pkgver = "4.18.6"
pkgrel = 2
build_style = "gnu_configure"
configure_args = ["--with-helper-path-prefix=/usr/libexec"]
# check target fails without this
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "glib-devel",
    "gobject-introspection",
    "gtk-doc-tools",
    "intltool",
    "libtool",
    "pkgconf",
    "xfce4-dev-tools",
]
makedepends = [
    "cairo-devel",
    "exo-devel",
    "garcon-devel",
    "glib-devel",
    "gtk+3-devel",
    "libdbusmenu-devel",
    "libwnck-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce panel"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://docs.xfce.org/xfce/xfce4-panel/start"
source = (
    f"$(XFCE_SITE)/xfce/xfce4-panel/{pkgver[:-2]}/xfce4-panel-{pkgver}.tar.bz2"
)
sha256 = "21337161f58bb9b6e42760cb6883bc79beea27882aa6272b61f0e09d750d7c62"
options = ["!cross"]


@subpackage("xfce4-panel-devel")
def _(self):
    return self.default_devel()
