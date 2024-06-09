pkgname = "xfce4-session"
pkgver = "4.18.4"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gmake",
    "iceauth",
    "intltool",
    "libtool",
    "pkgconf",
    "xfce4-dev-tools",
]
makedepends = [
    "libxfce4util-devel",
    "libxfce4ui-devel",
    "gtk+3-devel",
    "glib-devel",
    "libwnck-devel",
    "xfconf-devel",
    "polkit-devel",
    "libsm-devel",
]
depends = ["iceauth"]
pkgdesc = "Xfce desktop session"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/xfce/xfce4-session/start"
source = f"$(XFCE_SITE)/xfce/xfce4-session/{pkgver[:-2]}/xfce4-session-{pkgver}.tar.bz2"
sha256 = "9a9c5074c7338b881a5259d3b643619bf84901360c03478e1a697938ece06516"
