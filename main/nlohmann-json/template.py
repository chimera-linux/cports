pkgname = "nlohmann-json"
pkgver = "3.12.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DJSON_BuildTests=OFF"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "JSON for modern C++"
license = "MIT"
url = "https://json.nlohmann.me"
source = f"https://github.com/nlohmann/json/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4b92eb0c06d10683f7447ce9406cb97cd4b453be18d7279320f7b2f025c10187"
# header files
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.MIT")
