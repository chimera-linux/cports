pkgname = "orage"
pkgver = "4.18.0"
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
    "glib-devel",
    "gtk+3-devel",
    "libical-devel",
    "libnotify-devel",
    "libx11-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
]
pkgdesc = "Xfce time-managing app"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/apps/orage/start"
source = f"$(XFCE_SITE)/apps/orage/{pkgver[:-2]}/orage-{pkgver}.tar.bz2"
sha256 = "6313b49b26cfa39fc5e99468f3fbcfe0fa1c0f3f74273f03674f1a7d6141a3ec"
