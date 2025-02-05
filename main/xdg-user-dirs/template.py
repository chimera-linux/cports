pkgname = "xdg-user-dirs"
pkgver = "0.18"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "pkgconf",
    "automake",
    "libtool",
    "libxslt-progs",
    "docbook-xsl-nons",
    "gettext-devel",
]
pkgdesc = "Tool to help manage user directories"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "http://www.freedesktop.org/wiki/Software/xdg-user-dirs"
source = (
    f"https://user-dirs.freedesktop.org/releases/xdg-user-dirs-{pkgver}.tar.gz"
)
sha256 = "ec6f06d7495cdba37a732039f9b5e1578bcb296576fde0da40edb2f52220df3c"
