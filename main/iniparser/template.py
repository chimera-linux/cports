pkgname = "iniparser"
pkgver = "4.2.4"
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
sha256 = "cd4341a4dec5505e1f007cec643d064e8ad526569bd904f0e823c4a6ab10b8ba"
# vis breaks symbols
hardening = []


def post_install(self):
    self.install_license("LICENSE")


@subpackage("iniparser-devel")
def _devel(self):
    return self.default_devel()
