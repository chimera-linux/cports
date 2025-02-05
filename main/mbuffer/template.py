pkgname = "mbuffer"
pkgver = "20241007"
pkgrel = 0
build_style = "cmake"
make_dir = "."
hostmakedepends = ["cmake", "ninja"]
makedepends = [
    "linux-headers",
    "openssl3-devel",
]
pkgdesc = "Tool for buffering data streams"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-3.0-only"
url = "https://www.maier-komor.de/mbuffer.html"
source = f"https://www.maier-komor.de/software/mbuffer/mbuffer-{pkgver}.tgz"
sha256 = "9d7363010b4ef45b1646f6b5f5027b49bb6a209c502fb84e281c7bd771d56bed"


def pre_configure(self):
    self.do("sh", "mkversion.sh")
