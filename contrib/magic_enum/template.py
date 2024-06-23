pkgname = "magic_enum"
pkgver = "0.9.5"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DMAGIC_ENUM_OPT_BUILD_EXAMPLES=OFF"]
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
sha256 = "44ad80db5a72f5047e01d90e18315751d9ac90c0ab42cbea7a6f9ec66a4cd679"


def post_install(self):
    self.install_license("LICENSE")
