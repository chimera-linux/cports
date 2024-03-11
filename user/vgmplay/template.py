pkgname = "vgmplay"
pkgver = "0.51.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["libvgm-devel", "inih-devel"]
pkgdesc = "VGM file player"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "custom:vgmplay"
url = "https://github.com/ValleyBell/vgmplay-libvgm"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "6f9d4817dfb057193d9704e1c5b4aec6dc1226d97aea1bf66546a086e8f61aee"
options = ["!distlicense"]
restricted = "non-redistributable"


def post_install(self):
    # install default configuration
    self.install_file("VGMPlay.ini", "etc/vgmplay")
