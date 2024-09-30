pkgname = "mbuffer"
pkgver = "20240929"
pkgrel = 1
build_style = "cmake"
make_dir = "."
hostmakedepends = ["cmake", "ninja"]
makedepends = ["linux-headers"]
pkgdesc = "Tool for buffering data streams"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-3.0-only"
url = "https://www.maier-komor.de/mbuffer.html"
source = f"https://www.maier-komor.de/software/mbuffer/mbuffer-{pkgver}.tgz"
sha256 = "efb6c6de3e2459d2398774cdd44ec0a6e6b88c4132ede43d3d5e2f6c18d9a6a7"


def pre_configure(self):
    self.do("sh", "mkversion.sh")
