pkgname = "mediainfo"
pkgver = "24.05"
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
sha256 = "76edfaac4987c0784be1b059db82b8822207e208020ee2c79dab6f8785c3690d"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("../../../LICENSE")
