pkgname = "xfce4-taskmanager"
pkgver = "1.5.7"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "intltool",
    "libtool",
    "pkgconf",
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
sha256 = "6736832f5a64533e536f4994280bd907da19666cda8d2f465c8a53bb581f68bb"
