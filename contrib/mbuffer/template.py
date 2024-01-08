pkgname = "mbuffer"
pkgver = "20240107"
pkgrel = 0
build_style = "cmake"
make_dir = "."
hostmakedepends = ["cmake", "ninja", "bash", "linux-headers"]
pkgdesc = "Tool for buffering data streams"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-3.0-only"
url = "https://www.maier-komor.de/mbuffer.html"
source = f"https://www.maier-komor.de/software/{pkgname}/{pkgname}-{pkgver}.tgz"
sha256 = "d78606e17dd9026a53236d5ecc07a70202d2642d17e3d907471cdb58a0458814"


def pre_configure(self):
    self.do("bash", "mkversion.sh")
