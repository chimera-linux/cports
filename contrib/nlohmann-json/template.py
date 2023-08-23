pkgname = "nlohmann-json"
pkgver = "3.11.2"
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
sha256 = "d69f9deb6a75e2580465c6c4c5111b89c4dc2fa94e3a85fcd2ffcd9a143d9273"
# header files
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.MIT")
