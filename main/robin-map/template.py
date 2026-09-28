pkgname = "robin-map"
pkgver = "1.4.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCMAKE_POLICY_VERSION_MINIMUM=3.5"]
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Hash map and hash set implementation"
license = "MIT"
url = "https://github.com/Tessil/robin-map"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7930dbf9634acfc02686d87f615c0f4f33135948130b8922331c16d90a03250c"


def post_install(self):
    self.install_license("LICENSE")
