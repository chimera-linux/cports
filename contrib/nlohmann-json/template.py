pkgname = "nlohmann-json"
pkgver = "3.11.3"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "ninja",
    "pkgconf",
]
pkgdesc = "JSON for modern C++"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://json.nlohmann.me"
source = f"https://github.com/nlohmann/json/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0d8ef5af7f9794e3263480193c491549b2ba6cc74bb018906202ada498a79406"
# header files
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.MIT")
