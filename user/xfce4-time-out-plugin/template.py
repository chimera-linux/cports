pkgname = "xfce4-time-out-plugin"
pkgver = "1.2.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "gettext",
    "meson",
    "pkgconf",
]
makedepends = [
    "gtk+3-devel",
    "libx11-devel",
    "libxfce4ui-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce time-out panel plugin"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-time-out-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-time-out-plugin/{pkgver[:-2]}/xfce4-time-out-plugin-{pkgver}.tar.xz"
sha256 = "e344d9f82a8acd23d44e7cf9b2efe9599ffff856d9ba1a9be0e67b022c0d2eb2"
