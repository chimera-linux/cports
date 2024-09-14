pkgname = "xfdashboard"
pkgver = "1.0.0"
pkgrel = 1
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "glib-devel",
    "intltool",
    "libtool",
    "pkgconf",
    "xfce4-dev-tools",
]
makedepends = [
    "clutter-devel",
    "garcon-devel",
    "gtk+3-devel",
    "libwnck-devel",
    "libx11-devel",
    "libxcomposite-devel",
    "libxdamage-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "libxinerama-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce dashboard"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/apps/xfdashboard/start"
source = (
    f"$(XFCE_SITE)/apps/xfdashboard/{pkgver[:-2]}/xfdashboard-{pkgver}.tar.bz2"
)
sha256 = "a5284343e5ce09722f98d3b578588b36923e1ae5649754aa906980fdcdef48a5"


@subpackage("xfdashboard-devel")
def _(self):
    return self.default_devel()
