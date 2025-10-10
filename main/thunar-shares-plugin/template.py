pkgname = "thunar-shares-plugin"
pkgver = "0.5.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gettext",
    "meson",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
    "thunar-devel",
    "xfconf-devel",
]
pkgdesc = "Thunar shares plugin"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/xfce/thunar/thunar-shares-plugin"
source = f"$(XFCE_SITE)/thunar-plugins/thunar-shares-plugin/{pkgver[:-2]}/thunar-shares-plugin-{pkgver}.tar.xz"
sha256 = "34d4d69d413e63837c5083506b4dbf65f1fd2efe17667b1d7ad0699e1e2eb07d"
