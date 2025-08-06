pkgname = "mediainfo"
pkgver = "25.07"
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
sha256 = "e1b72bba16b23e5a83693bcbedd5104c87671490a634d8c3a8b12638f547c06f"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("../../../LICENSE")
