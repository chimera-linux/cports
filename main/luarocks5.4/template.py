pkgname = "luarocks5.4"
pkgver = "3.12.0"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--lua-version=5.4",
    "--prefix=/usr",
]
configure_gen = []
hostmakedepends = ["lua5.4", "unzip"]
makedepends = ["lua5.4-devel"]
depends = ["lua5.4-devel", "unzip"]
depends = ["lua5.4"]
pkgdesc = "Package manager for Lua modules"
license = "MIT"
url = "https://luarocks.org"
source = f"{url}/releases/luarocks-{pkgver}.tar.gz"
sha256 = "3d4c8acddf9b975e77da68cbf748d5baf483d0b6e9d703a844882db25dd61cdf"
# no tests defined
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
