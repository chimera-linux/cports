pkgname = "mediainfo"
pkgver = "23.11"
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
sha256 = "b4780a78d7af272d8b8a9a1bf226cc0827e74851fea73f63374cc78fdde227d0"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("../../../LICENSE")
