pkgname = "xdpyinfo"
pkgver = "1.3.4"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--without-dmx"]
hostmakedepends = ["pkgconf", "automake", "libtool", "xorg-util-macros"]
makedepends = [
    "libxext-devel",
    "libxtst-devel",
    "libxxf86vm-devel",
    "libxxf86misc-devel",
    "libxrender-devel",
    "libxcomposite-devel",
    "libxinerama-devel",
]
pkgdesc = "X display information utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xdpyinfo-{pkgver}.tar.gz"
sha256 = "fbd1e18885f67332b330fecd83592af25ad42d21457aaabfbd31a5a97388652a"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
