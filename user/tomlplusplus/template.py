pkgname = "tomlplusplus"
pkgver = "3.4.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "cmake",
    "meson",
    "pkgconf",
]
pkgdesc = "Header-only TOML config file parser and serializer for C++17"
license = "MIT"
url = "https://github.com/marzer/tomlplusplus"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "8517f65938a4faae9ccf8ebb36631a38c1cadfb5efa85d9a72e15b9e97d25155"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("tomlplusplus-devel")
def _(self):
    return self.default_devel()
