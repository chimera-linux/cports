pkgname = "mediainfo"
pkgver = "24.06"
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
sha256 = "082d1cfd316e9696a9dd3e2e3cb8303de3061e0387856d803417ba27097995ae"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("../../../LICENSE")
