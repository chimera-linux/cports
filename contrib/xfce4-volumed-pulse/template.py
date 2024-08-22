pkgname = "xfce4-volumed-pulse"
pkgver = "0.2.4"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
    "xfce4-dev-tools",
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
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-3.0-or-later"
# FIXME: Should be https://gitlab.xfce.org/apps/xfce4-volumed-pulse but that
# causes the update check to not find any versions, seems like some kind of race
# condition but not sure
url = "https://xfce.org"
source = f"$(XFCE_SITE)/apps/xfce4-volumed-pulse/{pkgver[:-2]}/xfce4-volumed-pulse-{pkgver}.tar.bz2"
sha256 = "a019e3f626b31c0aaa0b807962606645cc0caf7930882b034a5a3a1719858362"
