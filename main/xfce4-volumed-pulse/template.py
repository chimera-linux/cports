pkgname = "xfce4-volumed-pulse"
pkgver = "0.2.5"
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
sha256 = "30ebee3a16e467a2120db63b53d4cd3a603b310c6141c9514371c2dedf68bb03"
