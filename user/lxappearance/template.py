pkgname = "lxappearance"
pkgver = "0.6.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-gtk3"]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "intltool",
    "pkgconf",
]
makedepends = ["gtk+3-devel", "libx11-devel"]
pkgdesc = "Feature-rich GTK+ theme switcher"
maintainer = "jabuxas <jabuxas@proton.me>"
license = "GPL-2.0-or-later"
url = "https://github.com/lxde/lxappearance"
source = f"https://downloads.sourceforge.net/lxde/lxappearance-{pkgver}.tar.xz"
sha256 = "7222d858b8fef4b7967c42142d61e82ded6dd42dc5ef1d59caad775795928b38"
# no tests
options = ["!check"]
