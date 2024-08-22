pkgname = "gigolo"
pkgver = "0.5.3"
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
]
pkgdesc = "Xfce GIO/GVFS frontend"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-only"
url = "https://docs.xfce.org/apps/gigolo/start"
source = f"$(XFCE_SITE)/apps/gigolo/{pkgver[:-2]}/gigolo-{pkgver}.tar.bz2"
sha256 = "d25984f65744665e2433335249f9547a38cead45440027af0c397ebf254d2fd0"
