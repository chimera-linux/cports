pkgname = "lxrandr"
pkgver = "0.3.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-man", "--enable-gtk3"]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "intltool",
    "pkgconf",
]
makedepends = ["gtk+3-devel"]
pkgdesc = "LXDE monitor configuration tool"
maintainer = "jabuxas <jabuxas@proton.me>"
license = "GPL-2.0-or-later"
url = "https://github.com/lxde/lxrandr"
source = f"https://downloads.sourceforge.net/lxde/{pkgname}-{pkgver}.tar.xz"
sha256 = "8b5edfc9718061bc161fe51d388697cbaa819d6f8013ed24ba22f438e0dbc312"
