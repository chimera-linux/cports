pkgname = "tomlplusplus"
pkgver = "3.5.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dbuild_lib=true",
]
hostmakedepends = [
    "cmake",
    "meson",
    "pkgconf",
]
pkgdesc = "Header-only TOML config file parser and serializer for C++17"
license = "MIT"
url = "https://github.com/marzer/tomlplusplus"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4821c769370a6489b6a37814f16f3769eee0f2e733a5c129d5d99e2515a95c2b"


def post_install(self):
    self.install_license("LICENSE")


@split("devel")
def _(self):
    return self.default_devel()
