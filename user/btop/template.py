pkgname = "btop"
pkgver = "1.3.2"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBTOP_LTO=OFF", "-DBTOP_FORTIFY=OFF"]
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "TUI monitor of system resources"
maintainer = "mia <mia@mia.jetzt>"
license = "Apache-2.0"
url = "https://github.com/aristocratos/btop"
source = f"{url}/archive/v{pkgver}/btop-{pkgver}.tar.gz"
sha256 = "331d18488b1dc7f06cfa12cff909230816a24c57790ba3e8224b117e3f0ae03e"
hardening = ["cfi", "vis"]


# no tests, just make sure binary runs
def check(self):
    self.do("./build/btop", "--version")
