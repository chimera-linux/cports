pkgname = "rapidyaml"
pkgver = "0.16.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
]
hostmakedepends = [
    "cmake",
    "git",
    "ninja",
]
pkgdesc = "YAML parser/generator for C++"
license = "MIT"
url = "https://github.com/biojppm/rapidyaml"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ad4337d468c5f5d8624651bdc2900f7fe601c83fc3cff669dc972bf8634af4e9"


def post_install(self):
    self.install_license("LICENSE.txt")


@split("devel")
def _(self):
    return self.default_devel()
