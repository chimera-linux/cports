pkgname = "xfce4-places-plugin"
pkgver = "1.9.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "gettext",
    "meson",
    "pkgconf",
]
makedepends = [
    "exo-devel",
    "gtk+3-devel",
    "libnotify-devel",
    "libwnck-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfce4-panel-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce folders and media quick access panel plugin"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-places-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-places-plugin/{pkgver[:-2]}/xfce4-places-plugin-{pkgver}.tar.xz"
sha256 = "76d95687e0bea267465e832eea6266563a18d2219192f9e8af6f88e899262e43"
