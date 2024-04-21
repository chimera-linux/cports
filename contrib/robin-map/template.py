pkgname = "robin-map"
pkgver = "1.3.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Hash map and hash set implementation"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "MIT"
url = "https://github.com/Tessil/robin-map"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a8424ad3b0affd4c57ed26f0f3d8a29604f0e1f2ef2089f497f614b1c94c7236"


def post_install(self):
    self.install_license("LICENSE")
