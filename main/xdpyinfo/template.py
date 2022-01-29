pkgname = "xdpyinfo"
pkgver = "1.3.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--without-dmx"]
hostmakedepends = ["pkgconf"]
makedepends = [
    "libxext-devel", "libxtst-devel", "libxxf86vm-devel", "libxxf86misc-devel",
    "libxrender-devel", "libxcomposite-devel", "libxinerama-devel",
]
pkgdesc = "X display information utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.bz2"
sha256 = "30238ed915619e06ceb41721e5f747d67320555cc38d459e954839c189ccaf51"

def post_install(self):
    self.install_license("COPYING")
