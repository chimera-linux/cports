pkgname = "libfm"
pkgver = "1.3.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--enable-exif",
    "--enable-largefile",
    "--enable-udisks",
    "--with-gtk=3",
]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gtk-doc-tools",
    "intltool",
    "libtool",
    "pkgconf",
    "vala",
]
makedepends = [
    "dbus-devel",
    "glib-devel",
    "gtk+3-devel",
    "libexif-devel",
    "menu-cache",
    "libx11-devel",
]
pkgdesc = "Library for file management"
maintainer = "jabuxas <jabuxas@proton.me>"
license = "GPL-2.0-or-later"
url = "https://github.com/lxde/libfm"
source = f"https://downloads.sourceforge.net/pcmanfm/libfm-{pkgver}.tar.xz"
sha256 = "a5042630304cf8e5d8cff9d565c6bd546f228b48c960153ed366a34e87cad1e5"


@subpackage("libfm-devel")
def _(self):
    return self.default_devel()
