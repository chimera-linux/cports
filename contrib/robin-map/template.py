pkgname = "robin-map"
pkgver = "1.2.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Hash map and hash set implementation"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "MIT"
url = "https://github.com/Tessil/robin-map"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c72767ecea2a90074c7efbe91620c8f955af666505e22782e82813c652710821"


def post_install(self):
    self.install_license("LICENSE")
