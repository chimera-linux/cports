pkgname = "magic_enum"
pkgver = "0.9.7"
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
sha256 = "b403d3dad4ef542fdc3024fa37d3a6cedb4ad33c72e31b6d9bab89dcaf69edf7"


def post_install(self):
    self.install_license("LICENSE")
