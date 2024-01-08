pkgname = "mbuffer"
pkgver = "20231216"
pkgrel = 0
build_style = "cmake"
make_dir = "."
hostmakedepends = ["cmake", "ninja", "bash", "linux-headers"]
pkgdesc = "Tool for buffering data streams"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-3.0-only"
url = "https://www.maier-komor.de/mbuffer.html"
source = f"https://www.maier-komor.de/software/{pkgname}/{pkgname}-{pkgver}.tgz"
sha256 = "4a27f6621a06e7f3dd1a8846479d6b22e3212603f3bf825a0e8c93940bf7689c"


def pre_configure(self):
    self.do("bash", "mkversion.sh")
