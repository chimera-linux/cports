pkgname = "magic_enum"
pkgver = "0.9.6"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DMAGIC_ENUM_OPT_BUILD_EXAMPLES=OFF",
    "-DMAGIC_ENUM_OPT_INSTALL_PACKAGE_XML=OFF",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "Header-only library for enum reflection"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/Neargye/magic_enum"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "814791ff32218dc869845af7eb89f898ebbcfa18e8d81aa4d682d18961e13731"


def post_install(self):
    self.install_license("LICENSE")
