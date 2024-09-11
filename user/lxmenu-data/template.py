pkgname = "lxmenu-data"
pkgver = "0.1.6"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "intltool",
    "pkgconf",
]
makedepends = ["glib-devel"]
pkgdesc = "Provides files needed for LXDE application menus"
maintainer = "jabuxas <jabuxas@proton.me>"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxde/lxmenu-data"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "b237e732609fb2a521a942e08bb825ac7973ee478db7567d3606665a3793b2e8"
