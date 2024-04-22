pkgname = "mediainfo"
pkgver = "24.04"
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
sha256 = "e823505a27f41b45b5b3740ee16ff6b16cd2f9f6cc1f8ce2f308a1276a933cab"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("../../../LICENSE")
