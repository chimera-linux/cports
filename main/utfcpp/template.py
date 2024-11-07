pkgname = "utfcpp"
pkgver = "4.0.6"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "UTF-8 header-only library"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSL-1.0"
url = "https://github.com/nemtrif/utfcpp"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6920a6a5d6a04b9a89b2a89af7132f8acefd46e0c2a7b190350539e9213816c0"


def post_install(self):
    self.install_license("LICENSE")
