pkgname = "libfm-extra"
pkgver = "1.3.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-extra-only", "--disable-static"]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gtk-doc-tools",
    "intltool",
    "libtool",
    "pkgconf",
]
makedepends = ["glib-devel"]
pkgdesc = "Library for file management"
subdesc = " (extra library)"
maintainer = "jabuxas <jabuxas@proton.me>"
license = "GPL-2.0-or-later"
url = "https://github.com/lxde/libfm"
source = f"https://downloads.sourceforge.net/pcmanfm/libfm-{pkgver}.tar.xz"
sha256 = "a5042630304cf8e5d8cff9d565c6bd546f228b48c960153ed366a34e87cad1e5"
