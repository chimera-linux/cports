pkgname = "menu-cache"
pkgver = "1.1.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static"]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gtk-doc-tools",
    "intltool",
    "libtool",
    "pkgconf",
]
makedepends = ["gtk+3-devel", "libfm-extra", "libx11-devel"]
pkgdesc = "Caching mechanism for freedesktop.org compliant menus"
maintainer = "jabuxas <jabuxas@proton.me>"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxde/menu-cache"
source = f"https://downloads.sourceforge.net/lxde/menu-cache-{pkgver}.tar.xz"
sha256 = "ed02eb459dcb398f69b9fa5bf4dd813020405afc84331115469cdf7be9273ec7"
