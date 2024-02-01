pkgname = "mediainfo"
pkgver = "24.01.1"
pkgrel = 0
build_wrksrc = "Project/GNU/CLI"
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["libmediainfo-devel", "libzen-devel"]
pkgdesc = "Display information about media files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://mediaarea.net/en/MediaInfo"
source = f"https://mediaarea.net/download/source/mediainfo/{pkgver}/mediainfo_{pkgver}.tar.bz2"
sha256 = "c7a0bafb20f255071aac7173513bbc2c1d6a48b3cb051850809df8f6db62844a"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("../../../LICENSE")
