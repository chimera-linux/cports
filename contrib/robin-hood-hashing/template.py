pkgname = "robin-hood-hashing"
pkgver = "3.11.5"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DRH_STANDALONE_PROJECT=OFF"]
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Fast & memory efficient hashtable based on robin hood hashing"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "MIT"
url = "https://github.com/martinus/robin-hood-hashing"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "3693e44dda569e9a8b87ce8263f7477b23af448a3c3600c8ab9004fe79c20ad0"


def post_install(self):
    self.install_license("LICENSE")
