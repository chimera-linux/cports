pkgname = "xfce4-taskmanager"
pkgver = "1.5.8"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "pkgconf",
    "slibtool",
    "xfce4-dev-tools",
]
makedepends = [
    "cairo-devel",
    "glib-devel",
    "gtk+3-devel",
    "libwnck-devel",
    "libx11-devel",
    "libxfce4ui-devel",
    "libxmu-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce task manager"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/apps/xfce4-taskmanager/start"
source = f"$(XFCE_SITE)/apps/xfce4-taskmanager/{pkgver[:-2]}/xfce4-taskmanager-{pkgver}.tar.bz2"
sha256 = "14b9d68b8feb88a642a9885b8549efe7fc9e6c155f638003f2a4a58d9eb2baab"
