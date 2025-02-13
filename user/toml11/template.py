pkgname = "toml11"
pkgver = "4.4.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DTOML11_BUILD_TESTS=ON",
    "-DTOML11_BUILD_TOML_TESTS=ON",
]
hostmakedepends = ["cmake", "ninja"]
makedepends = ["doctest", "nlohmann-json"]
pkgdesc = "Feature-rich TOML language library for C++11/14/17/20"
maintainer = "Mathijs Rietbergen <mathijs.rietbergen@proton.me>"
license = "MIT"
url = "https://github.com/ToruNiina/toml11"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "815bfe6792aa11a13a133b86e7f0f45edc5d71eb78f5fb6686c49c7f792b9049"
hardening = ["!int"]  # when enabled, test_parse_integer fails...


def post_install(self):
    self.install_license("LICENSE")
