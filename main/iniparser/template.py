pkgname = "iniparser"
pkgver = "4.2.6"
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
license = "MIT"
url = "https://gitlab.com/iniparser/iniparser"
source = f"{url}/-/archive/v{pkgver}.tar.gz"
sha256 = "bbed169ed965a3673f58dd14164558832aaae92201f95e829d503f1da634e963"
# vis breaks symbols
hardening = []


def post_install(self):
    self.install_license("LICENSE")


@subpackage("iniparser-devel")
def _(self):
    return self.default_devel()
