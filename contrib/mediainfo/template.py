pkgname = "mediainfo"
pkgver = "24.03"
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
sha256 = "84c7c2358e415a01a2e56997713d4b3933b57104d04f76a6180ceed0abf4d3a0"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("../../../LICENSE")
