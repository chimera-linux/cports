pkgname = "mediainfo"
pkgver = "23.10"
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
sha256 = "8c058e16be1725eac0076fa32006bbe6b5c6197ef6feae6951fc56842a480807"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("../../../LICENSE")
