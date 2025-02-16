pkgname = "toml11"
pkgver = "4.3.0"
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
sha256 = "af95dab1bbb9b05a597e73d529a7269e13f1869e9ca9bd4779906c5cd96e282b"
hardening = ["!int"]  # when enabled, test_parse_integer fails...


def post_install(self):
    self.install_license("LICENSE")
