pkgname = "xfce4-volumed-pulse"
pkgver = "0.3.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "gettext",
    "meson",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
    "libkeybinder3-devel",
    "libnotify-devel",
    "libpulse-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce volume keys control daemon"
license = "GPL-3.0-or-later"
url = "https://gitlab.xfce.org/apps/xfce4-volumed-pulse"
source = f"$(XFCE_SITE)/apps/xfce4-volumed-pulse/{pkgver[:-2]}/xfce4-volumed-pulse-{pkgver}.tar.xz"
sha256 = "7031c3597d1a1e791afaf83a7b494b436aa54397ab1661e38ab32acb01c7fe85"
