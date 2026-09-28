pkgname = "mediainfo"
pkgver = "26.05"
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
sha256 = "fdf80b0ed37032091f066ce0c145765a5bc5b3be7b6e4a38d94ca7d96f77e2e6"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("../../../LICENSE")
