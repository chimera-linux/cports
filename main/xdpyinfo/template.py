pkgname = "xdpyinfo"
pkgver = "1.3.4"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--without-dmx"]
hostmakedepends = ["pkgconf", "automake", "libtool", "xorg-util-macros"]
makedepends = [
    "libxcomposite-devel",
    "libxext-devel",
    "libxinerama-devel",
    "libxrender-devel",
    "libxtst-devel",
    "libxxf86misc-devel",
    "libxxf86vm-devel",
]
pkgdesc = "X display information utility"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xdpyinfo-{pkgver}.tar.gz"
sha256 = "fbd1e18885f67332b330fecd83592af25ad42d21457aaabfbd31a5a97388652a"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
