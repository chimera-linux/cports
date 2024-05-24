pkgname = "iniparser"
pkgver = "4.2.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "doxygen",
    "ninja",
    "pkgconf",
]
checkdepends = ["bash"]
pkgdesc = "C library for INI file parsing"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://gitlab.com/iniparser/iniparser"
source = f"{url}/-/archive/v{pkgver}.tar.gz"
sha256 = "454bc88a4a508a43340a5c1b7e4d57f9b41a51d6ca5d72798fc7f32c435290bd"
# vis breaks symbols
hardening = []


def post_install(self):
    self.install_license("LICENSE")


@subpackage("iniparser-devel")
def _devel(self):
    return self.default_devel()
