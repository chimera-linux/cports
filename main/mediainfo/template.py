pkgname = "mediainfo"
pkgver = "24.12"
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
sha256 = "ca5b32d1ae8e7221274b183f1c79f12098c69f258e52551218dc33a3c81fd2ec"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("../../../LICENSE")
