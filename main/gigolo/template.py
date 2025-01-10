pkgname = "gigolo"
pkgver = "0.5.4"
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
]
pkgdesc = "Xfce GIO/GVFS frontend"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-only"
url = "https://docs.xfce.org/apps/gigolo/start"
source = f"$(XFCE_SITE)/apps/gigolo/{pkgver[:-2]}/gigolo-{pkgver}.tar.bz2"
sha256 = "29951a16ca48c5350fa862417a253bc45c2762106027c216bb7a56eabdd7f0f6"
