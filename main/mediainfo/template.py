pkgname = "mediainfo"
pkgver = "24.11"
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
sha256 = "739003ca623f0540f35a2ed7a3de3e77769b69fd36477c3eb9128960b5a248ac"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("../../../LICENSE")
