pkgname = "mediainfo"
pkgver = "24.11.1"
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
sha256 = "836d8c3609e007f85f93a1e8bee3c741ed5927838c843d1f7bc6f56a72fbc53f"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("../../../LICENSE")
