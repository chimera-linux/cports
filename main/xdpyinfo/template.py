pkgname = "xdpyinfo"
pkgver = "1.3.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--without-dmx"]
hostmakedepends = ["pkgconf"]
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
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.gz"
sha256 = "2ae7b8213ea839b8376843477496276e8d69550c48bff081e16376539fc27c5a"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")


configure_gen = []
