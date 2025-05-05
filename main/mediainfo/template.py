pkgname = "mediainfo"
pkgver = "25.04"
pkgrel = 0
build_wrksrc = "Project/GNU/CLI"
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["libmediainfo-devel", "libzen-devel"]
pkgdesc = "Display information about media files"
license = "BSD-2-Clause"
url = "https://mediaarea.net/en/MediaInfo"
source = f"https://mediaarea.net/download/source/mediainfo/{pkgver}/mediainfo_{pkgver}.tar.bz2"
sha256 = "157f7a2b0b6295ec2a411478d048a4431484a21abb028af901d5fc62f210518e"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("../../../LICENSE")
