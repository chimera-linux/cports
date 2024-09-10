pkgname = "pcmanfm"
pkgver = "1.3.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-gtk=3"]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "intltool",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "gtk+3-devel",
    "libfm-devel",
    "libx11-devel",
    "pango-devel",
]
depends = ["udisks"]
pkgdesc = "Fast lightweight tabbed file manager"
maintainer = "jabuxas <jabuxas@proton.me>"
license = "GPL-2.0-or-later"
url = "https://github.com/lxde/pcmanfm"
source = f"https://downloads.sourceforge.net/pcmanfm/pcmanfm-{pkgver}.tar.xz"
sha256 = "14cb7b247493c4cce65fbb5902611e3ad00a7a870fbc1e50adc50428c5140cf7"
# no tests
options = ["!check"]
