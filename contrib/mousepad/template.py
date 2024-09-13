pkgname = "mousepad"
pkgver = "0.6.2"
pkgrel = 1
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "libtool",
    "pkgconf",
    "xfce4-dev-tools",
]
makedepends = [
    "glib-devel",
    "gspell-devel",
    "gtk+3-devel",
    "gtksourceview4-devel",
    "libxfce4ui-devel",
    "polkit-devel",
]
pkgdesc = "Xfce text editor"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/apps/mousepad/start"
source = f"$(XFCE_SITE)/apps/mousepad/{pkgver[:-2]}/mousepad-{pkgver}.tar.bz2"
sha256 = "e7cacb3b8cb1cd689e6341484691069e73032810ca51fc747536fc36eb18d19d"
