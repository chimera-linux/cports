pkgname = "mediainfo"
pkgver = "23.09"
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
sha256 = "aeba3a11f2f48c62432f3a507208b80b4bb46b71f452b3fd3d7319b356dca5c8"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("../../../LICENSE")
