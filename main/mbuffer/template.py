pkgname = "mbuffer"
pkgver = "20240707"
pkgrel = 0
build_style = "cmake"
make_dir = "."
hostmakedepends = ["cmake", "ninja", "bash", "linux-headers"]
pkgdesc = "Tool for buffering data streams"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-3.0-only"
url = "https://www.maier-komor.de/mbuffer.html"
source = f"https://www.maier-komor.de/software/mbuffer/mbuffer-{pkgver}.tgz"
sha256 = "7f3926e92faa81b96a32420f80288b55f1850480f2a032c16ed61b53267cae09"


def pre_configure(self):
    self.do("bash", "mkversion.sh")
