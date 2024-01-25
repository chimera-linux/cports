pkgname = "utfcpp"
pkgver = "4.0.5"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "UTF-8 header-only library"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSL-1.0"
url = "https://github.com/nemtrif/utfcpp"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ffc668a310e77607d393f3c18b32715f223da1eac4c4d6e0579a11df8e6b59cf"


def post_install(self):
    self.install_license("LICENSE")
