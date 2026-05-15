pkgname = "mediainfo"
pkgver = "26.01"
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
sha256 = "61f948f8ae40ee4fb2f1cee4bee5ed193d5937603bf4e9f833862d3695fba7a9"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("../../../LICENSE")
