pkgname = "mediainfo"
pkgver = "23.07"
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
sha256 = "8e193f09972d8f70dd797cb2d34fe647e95e01f47b3f48c77d1dbed31359c5bf"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("../../../LICENSE")
