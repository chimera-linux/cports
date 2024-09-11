pkgname = "lxinput"
pkgver = "0.3.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-gtk3"]
# build fails without this
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "intltool",
    "pkgconf",
]
makedepends = ["gtk+3-devel", "libx11-devel"]
pkgdesc = "LXDE keyboard and mouse configuration"
maintainer = "jabuxas <jabuxas@proton.me>"
license = "GPL-2.0-or-later"
url = "https://github.com/lxde/lxinput"
source = f"https://downloads.sourceforge.net/lxde/{pkgname}-{pkgver}.tar.xz"
sha256 = "4e8f778a65a4afe2365b47e7899358aa4fab535343aa62c72a3cdc4cac1f6e88"
