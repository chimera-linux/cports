pkgname = "iniparser"
pkgver = "4.2.3"
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
sha256 = "99dad91ae3321759a401a22d998339457b1b2deffc39e20d89710b4d4cc3a7ae"
# vis breaks symbols
hardening = []


def post_install(self):
    self.install_license("LICENSE")


@subpackage("iniparser-devel")
def _devel(self):
    return self.default_devel()
